import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    room_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.room_text

    # ? timezone hasn't been changed, still the UTC time
    # instead of Europe/Helsinki
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Status(models.Model):
    # foreignkey status_set
    # related_manager that can create queryset
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=200)
    rates = models.IntegerField(default=0)

    def __str__(self):
        return self.status_text
