from base.helpers.google_sheets_api import GspReadApi
import random
from datetime import datetime
from gspread import utils


class SheetRandomizer:
    __WORKSHEET = 'Объявления'

    def __init__(self) -> None:
        self.__api = GspReadApi()

    def update_sheet(self, sheet_id: str) -> None:
        sheet = self.__api.open(sheet_id)
        worksheet = sheet.worksheet(self.__WORKSHEET)
        data = worksheet.get_all_values()

        if not len(data):
            raise ValueError('empty data')

        data = self.__randomize(data)
        if not (len(data) > 1 and len(data[0]) > 0):
            raise ValueError('empty randomized')

        address = utils.rowcol_to_a1(len(data), len(data[0]))
        address = 'A1:' + address
        worksheet.update(address, data)
        if len(data) == worksheet.row_count:
            worksheet.delete_rows(len(data), worksheet.row_count)
        else:
            worksheet.delete_rows(len(data) + 1, worksheet.row_count)

        worksheet.add_rows(10)

    def __randomize(self, sheet_data: list[list]) -> list[list]:
        headers_row = sheet_data[0]

        (index_title_spintax,
         index_description_spintax,
         index_price_spintax,
         index_title,
         index_description,
         index_price,
         index_bd,
         index_bt,
         index_ed,
         index_et,
         index_begin,
         index_end,
         index_timezone) = self.__get_header_indexes(
            headers_row,
            ['TitleSpintax',
             'DescriptionSpintax',
             'PriceSpintax',
             'Title',
             'Description',
             'Price',
             'BD',
             'BT',
             'ED',
             'ET',
             'DateBegin',
             'DateEnd',
             'TimeZone'])

        for row_idx, row in enumerate(sheet_data):
            if row_idx < 2: continue

            if row[index_title] == '' and row[index_title_spintax] != '':
                row[index_title] = self.__random_val(row, index_title_spintax)
                # print(1, self.__random_val(row, index_title_spintax))
            if not row[index_price] and row[index_price_spintax] != '':
                row[index_price] = self.__random_val(row, index_price_spintax)
            if row[index_description] == '' and row[index_description_spintax] != '':
                description = self.__random_val(row, index_description_spintax)
                if description.find('%Заголовок%') >= 0:
                    description = description.replace('%Заголовок%', row[index_title])
                if description.find('%Цена%') >= 0:
                    description = description.replace('%Цена%', row[index_price])
                row[index_description] = description

            # Обновление Дат

            timezone = 0
            if row[index_timezone] == 'Московское время':
                row[index_timezone] = 0
            if row[index_timezone] != '':
                timezone = int(row[index_timezone])

            if timezone == 0:
                timezone = '+03:00'
            else:
                bb = str(timezone)
                start = '+'
                if bb[0] == '-':
                    start = '-'
                    bb = bb[1:]
                timezone = start + '0' + bb + ':00'

            if row[index_bd] != '':
                if row[index_bt] == '':
                    date_b = row[index_bd]
                    date_b = datetime.strptime(date_b, "%d.%m.%Y")
                else:
                    date_b = row[index_bd] + '/' + row[index_bt]
                    date_b = datetime.strptime(date_b, "%d.%m.%Y/%H:%M:%S")
                date_b = date_b.isoformat() + timezone
                row[index_begin] = date_b

            if row[index_ed] != '':
                date_e = row[index_ed] + '/' + row[index_et]
                try:
                    date_e = datetime.strptime(date_e, "%d.%m.%Y/%H:%M:%S")
                    date_e = date_e.isoformat() + timezone
                    row[index_end] = date_e
                except ValueError:
                    pass

        return sheet_data

    def __random_val(self, row: list, spintax_index: int):
        res = ''
        spintax = row[spintax_index]
        new_txt = str(spintax).split('{')
        for row_txt in new_txt:
            if row_txt.find('}') <= 0:
                res += row_txt
                continue

            new_txt_2 = str(row_txt).split('}')
            arr = str(new_txt_2[0]).split('|')
            if not len(arr):
                continue

            res += arr[random.randint(0, len(arr) - 1)]
            if len(new_txt_2[1]) and new_txt_2[1][0] not in [" ", "!", ".", '\'', '']:
                res += ' '
            res += new_txt_2[1]
        return res

    def __get_header_indexes(self, headers_row: list, headers_names: list) -> list:
        indexes = [0] * len(headers_names)
        for header_idx, header_cell in enumerate(headers_row):
            for name_idx, header_name in enumerate(headers_names):
                if header_cell == header_name:
                    indexes[name_idx] = header_idx
                    break
        return indexes
