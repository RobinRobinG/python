from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from ..login.models import User


class Travel(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="trip_creator")
    participants=models.ManyToManyField(User, related_name="trip_participants")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)