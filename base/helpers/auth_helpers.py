from rest_framework.request import Request


class AuthHelper:
    def __init__(self, request: Request):
        self.__request = request

    def is_admin(self) -> bool:
        return self.is_authenticated() and self.__request.user.is_admin()

    def is_authenticated(self) -> bool:
        return self.__request.user.is_authenticated
