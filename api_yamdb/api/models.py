# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'


# class Genre(models.Model):
#     name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = 'Жанр'
#         verbose_name_plural = 'Жанры'


# class Title(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     genres = models.ManyToManyField(Genre, related_name='titles')

#     class Meta:
#         verbose_name = 'Произведение'
#         verbose_name_plural = 'Произведения'
