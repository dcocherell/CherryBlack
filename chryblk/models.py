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

class QuandlData(models.Model):
    ticker = models.CharField(max_length=10)  # for stock ticker symbols like 'AAPL', 'GOOGL', etc.
    date = models.DateField()
    open_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()  # assuming volume is an integer
    change = models.FloatField()
    average = models.FloatField(default=0.00)
    recommendation = models.CharField(default='Hold', max_length=10)

from django.db.models.signals import pre_save
from django.dispatch import receiver
from prometheus_client import Counter

DB_SAVES = Counter('db_saves_total', 'Database saves')

@receiver(pre_save)
def increment_db_saves(sender, instance, **kwargs):
    DB_SAVES.inc()