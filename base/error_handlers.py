from rest_framework.response import Response
from rest_framework.serializers import ValidationError
import logging


class ErrorHandler:
    def __init__(self, e: Exception) -> None:
        self.__error = e
        self.__logger = logging.getLogger('django')

    def handle(self) -> Response:
        self.__log()

        return self.__get_response()

    def __log(self) -> None:
        self.__logger.error(str(self.__error))

    def __get_response(self) -> Response:
        if isinstance(self.__error, ValidationError):
            return Response({'success': False, 'error_message': self.__error.detail})

        return Response({'success': False, 'error_message': str(self.__error)})
