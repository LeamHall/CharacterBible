from django.db import models
from django.urls import reverse
import uuid


class Character(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(max_length=25, default="FNU")
    last_name = models.CharField(max_length=35, default="LNU")
    notes = models.TextField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("character_detail", args=[str(self.id)])
