import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from users.models import Document


class Command(BaseCommand):
    help = 'populate the database with fake users and data for them'

    def add_arguments(self, parser):

        parser.add_argument(
            '--nodelete',
            action='store_true',
            help="Don't delete previously created database items",
        )

    def handle(self, *args, **options):

        if not options['nodelete']:
            # deleting all users should cause their data items to also be deleted
            User.objects.all().delete()

        # populate database with data from csv file
        data_file_path = os.path.join(os.getcwd(), 'src', 'users', 'data')
        user_csv_path = os.path.join(data_file_path, 'fake_users.csv')
        document_csv_path = os.path.join(data_file_path, 'fake_data.csv')
        # How to read CSV files in python
        # https://realpython.com/python-csv/#reading-csv-files-into-a-dictionary-with-csv
        try:
            self.stdout.write(f"getting data from {user_csv_path}")
            with open(user_csv_path, mode='r') as f:
                csv_reader = csv.DictReader(f)
                line_count = 0
                for row in csv_reader:
                    user = User.objects.create_user(
                                username=row['First Name'],
                                first_name=row['First Name'],
                                last_name=row['Last Name'],
                                email=row['Email'],
                                password=row['Password']
                                )
                    print(f"user: {user.username}, {user.password}")
                    print(f"user. first name: {row['First Name']}, Last Name: {row['Last Name']}")
                    line_count += 1

            self.stdout.write(f"getting data from {document_csv_path}")
            with open(document_csv_path, mode='r') as f:
                csv_reader = csv.DictReader(f)
                line_count = 0
                for row in csv_reader:
                    document = Document(
                                        user=User.objects.filter(email=row['user'])[0],
                                        title=row['title'],
                                        content=row['content']
                                        )
                    self.stdout.write(f"row: {row}")
                    self.stdout.write(f"user: {User.objects.filter(email=row['user'])[0]}")
                    self.stdout.write(f"{row['title']}: {row['content']}")
                    document.save()
                    line_count += 1

            self.stdout.write(self.style.SUCCESS("success?"))
            for document in User.objects.get(username='Nick').document_set.all():
                self.stdout.write(f"Nick's notes: {document.title}, {document.content}")
        except FileNotFoundError:
            raise CommandError("CSV File Not Found at specified directory")
