from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        if extra_fields.get('role', 0) != 1:
            raise ValueError("The role must be `customer`")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.email_verified_at = None
        user.email_verify_token = make_password(user.email + user.password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        if extra_fields.get('role', 1) != 0:  # admin_role == 0
            raise ValueError("The role must be `admin`")
        user = self.create_user(email, password, **extra_fields)
        user.email_verified_at = datetime.now()
        user.email_verify_token = None
        user.save()
        return user
