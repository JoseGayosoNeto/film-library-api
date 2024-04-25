from actors.models import Actor
import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'filename',
            type=str,
            help='Name of the CSV file containing the actors to be inserted'
        )

    def handle(self, *args, **options):
        filename = options['filename']

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                Actor.objects.create(
                    name=name,
                    date_of_birth=birthday,
                    nationality=nationality
                )

        self.stdout.write(self.style.SUCCESS('Actors added to database sucessfully'))