from django.contrib.auth.models import AbstractUser
from django.db import models
from .mangers import CustomUserManager


class CustomUser(AbstractUser):
    # Any additional fields you want to add
    email = models.EmailField(unique=True)

    # Assign the custom manager to objects
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Voting(models.Model):
    voters_name = models.CharField(max_length=200, null=True, blank=True)
    politician_name = models.CharField(max_length=200, null=True, blank=True)
    politician_position = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.politician_name

