from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Questions

# Create your tests here.

class QuestionsModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        #was_published_recently() returns False for questions whose pub_date is in the future.
        time = timezone.now() + datetime.timedelta(days=30)
        future_questions = Questions(pub_date = time)
        self.assertIs(future_questions.was_published_recently(), False)