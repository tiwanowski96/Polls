import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models.question import *

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question("Past question", -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: ID: 1, question_text: Past question>']
        )

    def test_future_question(self):
        create_question("Future question", 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], 
            []
        )
        self.assertContains(response, "No polls are available.")

    def test_future_and_past_questions(self):
        create_question("Past question", -30)
        create_question("Future question", 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: ID: 1, question_text: Past question>']
        )

    def test_two_past_questions(self):
        create_question("Past question 1.", -30)
        create_question("Past question 2.", -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: ID: 2, question_text: Past question 2.>', '<Question: ID: 1, question_text: Past question 1.>']
        )
