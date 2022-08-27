import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Room(models.Model):
    room_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.room_text

    # sorting the output of an arbitrary method
    @admin.display(
        boolean=True,
        ordering='pub_date',
        # rename the title of the column
        description='Published recently',
    )
    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        # <= now exclude future case
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Status(models.Model):
    # foreignkey status_set
    # related_manager that can create queryset
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=200)
    rates = models.IntegerField(default=0)

    def __str__(self):
        return self.status_text
    # fixing 'Statuss'
    class Meta:
        verbose_name_plural = 'Status'
