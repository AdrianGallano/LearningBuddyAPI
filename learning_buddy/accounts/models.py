from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return f"{str(self.pk)} - {self.username}"
