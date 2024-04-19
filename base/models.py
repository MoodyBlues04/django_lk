from __future__ import annotations
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    MIN_PASSWORD_LEN = 6

    class Role(models.IntegerChoices):
        ROLE_ADMIN = 0
        ROLE_CUSTOMER = 1

    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=255)
    role = models.IntegerField(choices=Role.choices)

    @classmethod
    def get_by_credentials(cls, username: str, password: str) -> User | None:
        user = User.get_by_username(username)
        return user if check_password(password, user.password) else None

    @classmethod
    def get_by_username(cls, username: str) -> User | None:
        return User.objects.filter(username=username).first()

    @classmethod
    def create(cls, username: str, password: str, role: int) -> User:
        return cls.objects.create(
            username=username,
            password=make_password(password),
            role=role,
        )

    @classmethod
    def is_valid_password(cls, password: str) -> bool:
        return len(password) >= cls.MIN_PASSWORD_LEN

    @classmethod
    def exists_with_username(cls, username: str) -> bool:
        return cls.get_by_username(username) is not None

    @classmethod
    def is_valid_role(cls, role: int) -> bool:
        return role in cls.Role

    def update_credentials(self, new_username: str, new_password: str) -> None:
        self.username = new_username
        self.password = new_password
        self.save()

    def is_admin(self) -> bool:
        return self.role == self.Role.ROLE_ADMIN
