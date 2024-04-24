from base.helpers.google_sheets_api import GoogleSheetsApi, GspReadApi


class GoogleSheetsService:
    __AVITO_SHEET_ID = '1lQ_XS4nAeQqsL_se1D9dfl9kFl3gbgxmLp-wr3qU00A'

    def __init__(self, sheet_id: str) -> None:
        self.__sheet_id = sheet_id
        self.__api = GoogleSheetsApi(sheet_id)

    @classmethod
    def copy_avito_sheet(cls) -> str:
        """ Copies default avito table, gives user perm to write and returns sheet id """
        return GspReadApi.copy(cls.__AVITO_SHEET_ID, 'Новая Таблица Avito')
