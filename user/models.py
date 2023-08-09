import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    username = None
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.guid.hex}"
