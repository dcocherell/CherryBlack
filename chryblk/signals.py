from django.core.signals import request_started
from django.dispatch import receiver
from .tasks import update_stocks

@receiver(request_started)
def run_my_task(sender, **kwargs):
    update_stocks()
