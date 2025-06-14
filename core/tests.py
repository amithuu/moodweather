from django.test import TestCase

# Create your tests here.# core/tests.py
from django.test import TestCase
from rest_framework.test import APIClient

class MoodWeatherTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_check_mood_weather(self):
        response = self.client.post('/api/check/', {"mood": "happy", "city": "Bangalore"}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("recommended_song", response.data)
