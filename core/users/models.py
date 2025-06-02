from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccounts(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """

    email = models.EmailField(unique=True, blank=False, null=False)