from django.contrib.auth import get_user_model
from reviews.models import Title, Category, Genre
from rest_framework import viewsets

from .serializers import (TitleSerializer,
                          CategorySerializer,
                          GenreSerializer,
                          UserSerializer)

User = get_user_model()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
