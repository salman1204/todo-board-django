import uuid

from django.db import models

from user.models import User

# Create your models here.


class Label(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title
