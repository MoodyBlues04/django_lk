from rest_framework import serializers
from base.models import User
from .auth_serializers import CredentialsAuthSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterUserSerializer(CredentialsAuthSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return User.create(
            username=validated_data['username'],
            password=validated_data['password'],
            role=User.Role.ROLE_CUSTOMER
        )

    def validate_username(self, username: str) -> str:
        if not User.exists_with_username(username):
            raise serializers.ValidationError('Username should be unique')
        return username

    def validate_password(self, password: str) -> str:
        if not User.is_valid_password(password):
            raise serializers.ValidationError(f'Password must be at least {User.MIN_PASSWORD_LEN} characters')
        return password


class LoginUserSerializer(CredentialsAuthSerializer):
    pass


class UpdateUserCredentialsSerializer(CredentialsAuthSerializer):
    new_username = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)

    def validate_new_username(self, new_username: str) -> str:
        user = User.get_by_username(new_username)
        if user is not None:
            raise serializers.ValidationError('Username should be unique')
        return new_username

    def validate_new_password(self, new_password: str) -> str:
        if not User.is_valid_password(new_password):
            raise serializers.ValidationError(f'Password must be at least {User.MIN_PASSWORD_LEN} characters')
        return new_password

    def update_credentials(self) -> None:
        user = self.get_authorized_user()
        user.update_credentials(
            self.data['new_username'],
            self.data['new_password']
        )
