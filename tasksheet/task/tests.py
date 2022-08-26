from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Room

# Create your tests here.
class RoomModelTests(TestCase):
    def test_was_published_recently_with_future_room(self):
        # for testing the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_room = Room(pub_date=time)

        self.assertIs(future_room.was_published_recently(), False)

    def test_was_published_recently_with_old_room(self):
        # over one day (one day and one second)
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_room = Room(pub_date=time)
        self.assertIs(old_room.was_published_rencently(), False)

    def test_was_published_recently_with_recent_question(self):
        # less than one day - goes back in time
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_room = Room(pub_date=time)
        self.assertIs(recent_room.was_published_recently(), True)




# end
