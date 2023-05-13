# api_yamdb
api_yamdb

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

_Установка_

Для того чтобы развернуть проект на локальном устройстве необходимо выполнить следующие шаги:

1. Склонирйте этот репозиторий: `git clone https://github.com/mogubudu/api_yamdb.git`
2. Перейдите в директорию с проектом: `cd api_yamdb`
3. Создайте виртуальное окружение: `python -m venv venv`
4. Активируйте виртуальное окружение: `source env/bin/activate` (для Linux), `source venv/Scripts/activate` (для Windows)
5. Установите зависимости из requirements.txt: `pip install -r requirements.txt`
6. Запустите миграции: `python manage.py migrate`
7. Запустите сервер: `python manage.py runserver`
