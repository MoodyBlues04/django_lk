from base.helpers.google_sheets_api import GoogleSheetsApi


class SheetRandomizer:
    __WORKSHEET = 'Объявления'

    def __init__(self, sheet_id: str) -> None:
        self.__api = GoogleSheetsApi(sheet_id)
        self.__api.set_worksheet(self.__WORKSHEET)

    def update_sheet(self) -> None:
        data = self.__api.sheet.worksheet.get_all_values()
        raise ValueError(data)
        # 1) get sheet data by api
        # 2) randomize
        # 3) just write it back
        pass

    def __randomize(self, sheet_data: list[list]) -> list[list]:
        pass
