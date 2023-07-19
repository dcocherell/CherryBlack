from django.test import TestCase, Client
from django.urls import reverse

class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_submission_flow(self):
        # Test GET request
        response = self.client.get(reverse('user_input'))
        self.assertEqual(response.status_code, 200)

        # Test POST request
        response = self.client.post(reverse('user_input'), {'text_input': 'Integration test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Integration test', response.content.decode())
