from base.helpers.google_sheets_api import GspReadApi


class SheetRandomizer:
    __WORKSHEET = 'Объявления'

    def __init__(self) -> None:
        self.__api = GspReadApi()

    def update_sheet(self, sheet_id: str) -> None:
        sheet = self.__api.open(sheet_id)
        worksheet = sheet.worksheet(self.__WORKSHEET)
        data = worksheet.get_all_values()
        raise ValueError(data)
        # 1) get sheet data by api
        # 2) randomize
        # 3) just write it back
        pass

    def __randomize(self, sheet_data: list[list]) -> list[list]:
        pass
