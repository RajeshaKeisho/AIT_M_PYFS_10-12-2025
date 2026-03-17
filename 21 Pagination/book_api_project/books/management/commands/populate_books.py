from django.core.management.base import BaseCommand
from faker import Faker
from books.models import Book
import random

class Command(BaseCommand):
    help = "Populate Books"
    def handle(self, *args, **kwargs):
        fake = Faker()
        genres = ["Fiction", "Non-Fiction", "Science-Fiction", "Fantsy", "Mystery", "Thriller", "Romance"]

        for _ in range(100):
            Book.objects.create(
                title = fake.catch_phrase(),
                author = fake.name(),
                publication_date = fake.date_this_century(),
                genre = random.choice(genres)
            )

        self.stdout.write(self.style.SUCCESS("Books Data Created Successfully!!"))
        