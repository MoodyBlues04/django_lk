from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        if extra_fields.get('role', 0) != 1:
            raise ValueError("The role must be `admin`")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        if extra_fields.get('role', 1) != 0:  # admin_role == 0
            raise ValueError("The role must be `admin`")
        return self.create_user(email, password, **extra_fields)
