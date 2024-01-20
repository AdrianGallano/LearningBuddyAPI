from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{str(self.pk)} - {self.username}"
