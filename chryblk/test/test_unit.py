from django.test import TestCase, Client
from django.urls import reverse

class UserInputTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_input_GET(self):
        # Test GET request
        response = self.client.get(reverse('user_input'))
        self.assertEqual(response.status_code, 200)

    def test_user_input_POST(self):
        # Test POST request
        response = self.client.post(reverse('user_input'), {'text_input': 'Test string'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test string', response.content.decode())
