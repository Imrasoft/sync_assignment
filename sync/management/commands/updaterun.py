
from django.core.management import BaseCommand
from sync.models import Run

__author__ = 'kenneth'


class Command(BaseCommand):
    def handle(self, *args, **options):
        added = Run.add_runss()
        self.stdout.write(self.style.SUCCESS('Successfully added %d groups' % added))
