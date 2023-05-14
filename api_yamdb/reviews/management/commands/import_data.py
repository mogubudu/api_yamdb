import csv
import os
from django.core.management.base import BaseCommand
from models import Category, Genre, Title, Review, User, Comment

# Словарь соответствия моделей файлам CSV
models = {
    'category.csv': Category,
    'genre.csv': Genre,
    # 'genre_title.csv': Title, #не уверен в данном виде связи
    'titles.csv': Title,
    'review.csv': Review,
    'users.csv': User,
    'comments.csv': Comment
}


class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('files', nargs='+', type=str)
        
    def handle(self, *args, **options):
        files = options['files']

        for file_name in files:
            file_path = os.path.join('static/data', file_name)
            if file_name not in models.keys():
                self.stderr.write('File not supported: %s' % file_name)
                continue
            model = models[file_name]
            with open(file_path) as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    instance = model()
                    for i, field in enumerate(model._meta.fields):
                        setattr(instance, field.name, row[i])
                    instance.save()
