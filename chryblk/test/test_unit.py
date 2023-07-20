from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from chryblk.models import FinancialData
import datetime

class InputFinancialDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.data = {
            'date': datetime.date.today(),
            'income': 5000.00,
            'expense': 2000.00,
            'expense_type': 'Rent',
            'state': 'CA'
        }

    def test_input_financial_data(self):
        response = self.client.post(reverse('chryblk:input_financial_data'), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FinancialData.objects.filter(income=5000.00).exists())


class ReportTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        FinancialData.objects.create(user=self.user, date=datetime.date.today(), income=5000, expense=2000.00, expense_type='Rent', state='CA')

    def test_report(self):
        response = self.client.get(reverse('chryblk:report'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '5000')