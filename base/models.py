from __future__ import annotations
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    MIN_PASSWORD_LEN = 6

    class Role(models.IntegerChoices):
        ROLE_ADMIN = 0
        ROLE_CUSTOMER = 1

    class Profession(models.TextChoices):
        AVITOLOG = "авитолог"
        MANAGER = "менеджер"

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=255, null=False)
    role = models.IntegerField(choices=Role.choices, null=False, default=Role.ROLE_CUSTOMER)
    phone = models.CharField(max_length=15, null=True, default=None)  # TODO phone-validator lib
    company = models.CharField(max_length=255, null=True, default=None)
    profession = models.CharField(max_length=255, choices=Profession.choices, default=Profession.AVITOLOG)
    tg = models.CharField(max_length=255, null=True, default=None)
    image = models.CharField(max_length=255, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'role']

    objects = UserManager()

    @classmethod
    def get_by_credentials(cls, email: str, password: str) -> User | None:
        return authenticate(username=email, password=password)

    @classmethod
    def get_by_email(cls, email: str) -> User | None:
        return User.objects.filter(email=email).first()

    @classmethod
    def is_valid_password(cls, password: str) -> bool:
        return len(password) >= cls.MIN_PASSWORD_LEN

    @classmethod
    def exists_with_email(cls, email: str) -> bool:
        return cls.get_by_email(email) is not None

    @classmethod
    def is_valid_role(cls, role: int) -> bool:
        return role in cls.Role

    def is_admin(self) -> bool:
        return self.role == self.Role.ROLE_ADMIN
