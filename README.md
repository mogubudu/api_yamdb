# api_yamdb

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

## Установка

Для того чтобы развернуть проект на локальном устройстве необходимо выполнить следующие шаги:

1. Склонирйте этот репозиторий: `git clone https://github.com/mogubudu/api_yamdb.git`
2. Перейдите в директорию с проектом: `cd api_yamdb`
3. Создайте виртуальное окружение: `python -m venv venv`
4. Активируйте виртуальное окружение: `source env/bin/activate` (для Linux), `source venv/Scripts/activate` (для Windows)
5. Установите зависимости из requirements.txt: `pip install -r requirements.txt`
6. Запустите миграции: `python manage.py migrate`
7. Запустите сервер: `python manage.py runserver`

Для использования функционала API необходимо отправлять HTTP-запросы на соответствующие эндпойнты. Документация по API доступна в ReDoc, которая расположена по адресу `http://localhost:8000/redoc/`.

Для доступа к защищенным эндпойнтам необходимо предоставить токен аутентификации, который можно получить на эндпойнте `/api/token/`.

## Примеры использования API:

**Получение списка произведений**

Для получения списка произведений можно воспользоваться эндпойнтом `/api/v1/titles/`. В ответ на запрос будет возвращен список произведений с их основными характеристиками (название, год выпуска, категория, жанры, рейтинг).
Запрос:
```
GET /api/v1/titles/
```

**Получение списка произведений с фильтрацией**

Чтобы получить список произведений с возможностью фильтрации по жанрам, категории и рейтингу, можно отправить GET-запрос на `/api/v1/titles/` с параметрами `genre`, `category` и `rating`, соответственно. Ниже приведен пример запроса с фильтрацией по жанру.
Запрос: 
```
GET /api/v1/titles/?genre=Action
```

**Создание отзыва**

Чтобы создать отзыв на произведение, нужно отправить POST-запрос на `/api/v1/titles/{title_id}/reviews/`. В теле запроса должны быть указаны оценка и текст отзыва.
Запрос: 
```
POST /api/v1/titles/1/reviews/
Authorization: Bearer access_token
Content-Type: application/json
{
    "score": 9,
    "text": "Great movie!"
}
```
Больше примеров вы можете найти, развернув проект локально - документация находится по адресу http://127.0.0.1:8000/redoc/

## Проект выполняли:
* Пипкин Владислав - тимлид, 1 разработчик
* Иванов Георгий - 2 разработчик
* Кузьмин Максим - 3 разработчик
