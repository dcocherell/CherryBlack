from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from chryblk.models import FinancialData
import datetime

class UserFlowTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.data = {
            'username': 'testuser',
            'password': '12345'
        }
        self.fin_data = {
            'date': datetime.date.today(),
            'income': 5000.00,
            'expense': 2000.00,
            'expense_type': 'Rent',
            'state': 'CA'
        }

    def test_user_flow(self):
        # User login
        response = self.client.post(reverse('chryblk:login'), self.data)
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after login

        # Input financial data
        response = self.client.post(reverse('chryblk:input_financial_data'), self.fin_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FinancialData.objects.filter(income=5000).exists())

        # Accessing the report page
        response = self.client.get(reverse('chryblk:report'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '5000')
