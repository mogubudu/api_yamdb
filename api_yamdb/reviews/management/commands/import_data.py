import csv

from django.core.management import BaseCommand
from django.db import IntegrityError

from api_yamdb.settings import BASE_DIR
from reviews.models import Category, Comment, Genre, TitleGenre, Review, Title, User

TABLES = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
    TitleGenre: 'genre_title.csv',
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for model, csv_f in TABLES.items():
            with open(
                f'{BASE_DIR}/static/data/{csv_f}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                try:
                    model.objects.bulk_create(model(**data) for data in reader)
                except ValueError:
                    self.stdout.write(
                        self.style.ERROR(
                            'Переименуйте, пожалуйста, значение category, '
                            'author добавив к ним _id.'
                            'Должно получиться: category_id, author_id'))
                except IntegrityError:
                    self.stdout.write(
                        self.style.ERROR(
                            'Ошибка базы данных, возможно вы уже добавили '
                            'значения из этих файлов.'
                        ))
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))