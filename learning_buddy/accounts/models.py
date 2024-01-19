from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(default="NoName", max_length=32, unique=True)
    email = models.EmailField(blank=False, unique=True, max_length=100)

    def __str__(self):
        return f"{str(self.pk)} - {self.username}"
