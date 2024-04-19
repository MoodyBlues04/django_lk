from rest_framework import serializers
from base.models import User


class CredentialsAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        self.__validate_credentials(attrs)
        return super().validate(attrs)

    def get_authorized_user(self) -> User:
        return User.get_by_credentials(username=self.data['username'], password=self.data['password'])

    def __validate_credentials(self, attrs) -> None:
        if User.get_by_credentials(attrs['username'], attrs['password']) is None:
            raise serializers.ValidationError(f"Check your credentials, user with such username and password not found")