import csv
import os

from django.core.management import BaseCommand

from api_yamdb.settings import BASE_DIR
from reviews.models import (Category, Comment,
                            Genre, TitleGenre,
                            Review, Title, User)

FILE_DIR = f'{BASE_DIR}/static/data/'

models_table = {
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
        for model, file_name in models_table.items():
            file_path = f'{FILE_DIR}/{file_name}'

            if not os.path.exists(file_path):
                self.stdout.write(
                    self.style.ERROR(
                        f'{file_name} отсутствует среди файлов'
                    )
                )
                continue

            with open(file_path, 'r+', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                if 'category' in reader.fieldnames:
                    replace_index = reader.fieldnames.index('category')
                    reader.fieldnames[replace_index] = 'category_id'
                if 'author' in reader.fieldnames:
                    replace_index = reader.fieldnames.index('author')
                    reader.fieldnames[replace_index] = 'author_id'
                try:
                    model.objects.bulk_create(model(**data) for data in reader)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Данные из {file_name} успешно загружены'
                        )
                    )
                except Exception as error:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Данные из {file_name} '
                            f'загрузить не удалось: {error}'
                        )
                    )
