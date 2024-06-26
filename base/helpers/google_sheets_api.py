from os import getenv
import pygsheets
import json
import gspread


class GoogleSheetsApi:
    def __init__(self, sheet_id: str) -> None:
        service_file = getenv('GOOGLE_API_CREDENTIALS_PATH')
        self.__client = pygsheets.authorize(service_file=service_file)
        self.__sheet = self.__client.open_by_key(sheet_id)
        self.__worksheet = None

    @property
    def sheet(self):
        return self.__sheet

    @property
    def worksheet(self):
        return self.__worksheet

    def set_worksheet(self, title: str) -> None:
        try:
            self.__worksheet = self.__sheet.worksheet_by_title(title)
        except pygsheets.exceptions.WorksheetNotFound:
            self.__worksheet = self.__sheet.add_worksheet(title, rows=1000)

    def clear_worksheet(self, start: str|tuple) -> None:
        self.__worksheet.clear(start=start)

    def increase_rows_count(self, add_rows: int) -> None:
        self.__worksheet.add_rows(add_rows)

    def get_rows_count(self) -> int:
        return self.__worksheet.rows

    def add_rows(self, rows: list[list]) -> None:
        """ Adds rows at the bottom of existing rows """

        row_idx = self.get_first_empty_row()
        for row in rows:
            self.set_row(row_idx, row)
            row_idx += 1

    def add_to_col(self, col: int, data: list) -> None:
        first_empty_row_idx = self.get_first_empty_row(col)
        self.set_col(col, data, start_row=first_empty_row_idx)

    def set_col(self, col: int, data: list, start_row: int = 2) -> None:
        for idx, el in enumerate(data):
            self.__worksheet.update_value((start_row + idx, col), el)

    def set_row(self, row: int, row_data: list) -> None:
        self.__worksheet.update_row(row, row_data)

    def is_set_row(self, row: int) -> bool:
        row_list = self.get_row(row)
        return len(row_list) > 0

    def get_row(self, row: int, return_as: str = 'cell'):
        return self.__worksheet.get_row(row, return_as, include_tailing_empty=False)

    def get_values(self, start: tuple, end: tuple) -> list:
        return self.__worksheet.get_values(start, end)

    def get_first_empty_row(self, col: int = 1) -> int:
        col_data = self.get_col(col)
        return len(col_data) + 1

    def get_col(self, col: int, return_as: str = 'cell'):
        return self.__worksheet.get_col(col, return_as, include_tailing_empty=False)

    def get_cell(self, row: int, col: int):
        return self.__worksheet.cell((row, col)).value

    def find_in_row(self, target, row: int) -> int|None:
        """ Returns column of found value """
        for idx, el in enumerate(self.get_row(row)):
            if el.value == target:
                return idx + 1
        return None

    def share(self, email_or_domain: str, role: str = 'writer', _type: str = 'user') -> None:
        self.__sheet.share(email_or_domain, role=role, type=_type)


class GspReadApi:
    def __init__(self) -> None:
        service_file = getenv('GOOGLE_API_CREDENTIALS_PATH')
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        credentials = json.load(open(service_file))

        self.__client = gspread.service_account_from_dict(credentials, scopes)
        self.__client.set_timeout(timeout=40)

    def copy(self, src_sheet_id: str, desc_title: str) -> str:
        """ Returns created sheet id """
        sheet = self.__client.copy(file_id=src_sheet_id, title=desc_title, copy_permissions=False)
        sheet.share(None, perm_type='anyone', role='writer')
        return sheet.id

    def open(self, sheet_id: str):
        return self.__client.open_by_key(sheet_id)
