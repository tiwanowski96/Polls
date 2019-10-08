import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models.question import *

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question('Future question.', 5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question('Past question.', -5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)