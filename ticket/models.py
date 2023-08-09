import uuid

from django.db import models

from label.models import Label
from user.models import User

# Create your models here.


class Ticket(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    expiry_date = models.DateField()

    def __str__(self):
        return self.title
