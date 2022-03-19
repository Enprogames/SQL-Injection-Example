from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'hash a given password'

    def add_arguments(self, parser):
        parser.add_argument('words', nargs='+', type=int)

    def handle(self, *args, **options):
        for word in options['words']:
            self.stdout.write(f"{word}: {make_password(str(word))}")
