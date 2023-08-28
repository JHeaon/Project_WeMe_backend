from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        user = self.create_user(email, password, **other_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_user(self, email, password, **other_fields):
        if self.validate(email, password):
            user = self.model(email=self.normalize_email(email), **other_fields)
            user.set_password(password)
            user.save()

            return user

    def validate(self, email, password):
        if email is None:
            raise TypeError("Users must have an email address.")
        elif password is None:
            raise TypeError("Users must have a password.")
        return True


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["phone_number"]

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email
