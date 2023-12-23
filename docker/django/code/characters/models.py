from django.db import models
from django.urls import reverse
import uuid


class Character(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    notes = models.TextField()

    def __str__(self):
        if not self.first_name:
            self.first_name = "FNU"
        if not self.last_name:
            self.last_name = "LNU"
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("character_detail", args=[str(self.id)])
