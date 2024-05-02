from base.helpers.google_sheets_api import GspReadApi


class GoogleSheetsService:
    __AVITO_SHEET_ID = '1lQ_XS4nAeQqsL_se1D9dfl9kFl3gbgxmLp-wr3qU00A'

    @classmethod
    def copy_avito_sheet(cls) -> str:
        """ Copies default avito table, gives user perm to write and returns sheet id """
        return GspReadApi().copy(cls.__AVITO_SHEET_ID, 'Новая Таблица Avito')
