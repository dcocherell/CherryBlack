import asyncio
from django.core.management.base import BaseCommand
from chryblk.tasks import update_stocks

class Command(BaseCommand):
    help = 'Starts the update_stocks task'

    def handle(self, *args, **options):
        self.stdout.write('Starting update_stocks task...')
        asyncio.run(update_stocks())
        self.stdout.write('update_stocks task started.')
