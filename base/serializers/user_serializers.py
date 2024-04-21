from rest_framework import serializers
from base.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AuthSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def get_authorized_user(self) -> User:
        return User.get_by_credentials(email=self.data['email'], password=self.data['password'])


class RegisterUserSerializer(AuthSerializer):
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    password_repeat = serializers.CharField()

    def validate(self, attrs: dict):
        if attrs.get('password') != attrs.get('password_repeat'):
            raise serializers.ValidationError("Password and repeated password are not equals")
        return super().validate(attrs)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_customer(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=User.Role.ROLE_CUSTOMER
        )

    def validate_email(self, email: str) -> str:
        if User.exists_with_email(email):
            raise serializers.ValidationError('Username should be unique')
        return email

    def validate_password(self, password: str) -> str:
        if not User.is_valid_password(password):
            raise serializers.ValidationError(f'Password must be at least {User.MIN_PASSWORD_LEN} characters')
        return password


class LoginUserSerializer(AuthSerializer):
    def validate(self, attrs: dict):
        user = User.get_by_credentials(attrs['email'], attrs['password'])
        if user is None:
            raise serializers.ValidationError(f"Invalid credentials: {attrs['email']} {attrs['password']} {user}")
        return super().validate(attrs)


class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    phone = serializers.CharField(allow_null=True)
    company = serializers.CharField(allow_null=True)
    profession = serializers.CharField(allow_null=False)
    tg = serializers.CharField(allow_null=True)
    # image = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        return User.objects.create()

    def update(self, instance: User, validated_data: dict) -> None:
        instance.email = validated_data['email']
        instance.phone = validated_data['phone']
        instance.username = validated_data['username']
        instance.company = validated_data['company']
        instance.profession = validated_data['profession']
        instance.tg = validated_data['tg']
        # instance.image = validated_data['image']
        instance.save()
