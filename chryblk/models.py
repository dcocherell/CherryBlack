from django.db import models
from django.conf import settings

# Create your models here.
class FinancialData(models.Model):
    date = models.DateField()
    income = models.FloatField()
    expense = models.FloatField()
    expense_type = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

