from __future__ import annotations

import json

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    MIN_PASSWORD_LEN = 6

    class Role(models.IntegerChoices):
        ROLE_ADMIN = 0, 'admin'
        ROLE_CUSTOMER = 1, 'customer'

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
    email_verify_token = models.CharField(max_length=255, null=True, default=None)
    email_verified_at = models.DateTimeField(null=True, default=None)

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

    @property
    def role_label(self) -> str:
        return self.Role(self.role).label


class Project(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'inactive'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=255, null=False, choices=Status.choices)
    sheet_id = models.CharField(max_length=255, null=False)
    xml_id = models.CharField(max_length=255, null=False)
    time_web_token = models.CharField(max_length=255, null=False)
    avito_client_id = models.CharField(max_length=255, null=False)
    avito_client_secret = models.CharField(max_length=255, null=False)
    image = models.CharField(max_length=255, null=True, default=None)
    bucket = models.CharField(max_length=255, null=True, default=None)


class Tariff(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    price = models.PositiveIntegerField(default=0, null=False)
    options = models.JSONField()


class Payment(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created'
        IN_PROGRESS = 'in_progress'
        PAID = 'paid'
        FAILED = 'failed'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=Status.choices, null=False)
    sum = models.PositiveIntegerField(null=False, default=0)
    description = models.CharField(max_length=255, null=False, blank=True)


class Subscription(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'inactive'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True)
    period_start = models.DateField()
    period_end = models.DateField()
    status = models.CharField(max_length=255, null=False, choices=Status.choices)
    remaining_options = models.JSONField()


class FAQ(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    content = models.CharField(max_length=1024, null=False, blank=True)
    links = models.JSONField()
    is_active = models.BooleanField(default=False, null=False)

    @property
    def links_dict(self) -> dict:
        return json.loads(self.links)

    @property
    def links_text(self) -> str:
        res = ''
        for label, link in self.links_dict.items():
            res += f'{label} {link}\n'
        res = res.rstrip()
        return res
