from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from api_yamdb.settings import SERVICE_EMAIL
from rest_framework import filters, viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response

from reviews.models import Title, Category, Genre
from .serializers import (TitleSerializer,
                          CategorySerializer,
                          GenreSerializer,
                          UserSerializer,
                          GetTokenSerializer,
                          SignUpSerializer, UserProfileSerializer)
from .permissions import isAdmin

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
    permission_classes = [isAdmin]
    lookup_field = 'username'
    filter_backends = [filters.SearchFilter]
    search_fields = ('username',)
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(detail=False, methods=('get',),
            url_path='me', url_name='me',
            permission_classes=(permissions.IsAuthenticated,))
    def profile(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @profile.mapping.patch
    def patch_profile(self, request):
        serializer = UserProfileSerializer(
            request.user,
            data=request.data,
            partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    serializer = GetTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    confirmation_code = serializer.validated_data.get('confirmation_code')
    user = get_object_or_404(User, username=username)

    if default_token_generator.check_token(user, confirmation_code):
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response(
        {'confirmation_code': 'Неверный код подтверждения'},
        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_confirmation_code(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    try:
        user, is_created = User.objects.get_or_create(
            email=email,
            username=username)
    except IntegrityError:
        return Response(
            'Электронная почта или имя пользователя уже используется.',
            status=status.HTTP_400_BAD_REQUEST)

    confirmation_code = default_token_generator.make_token(user)
    mail_subject = 'Ваш код подтверждения для API_YAMBD'
    message = (f'Добро пожаловать на борт!\n'
               f'Ваш код подтверждения: {confirmation_code}')
    send_mail(
        mail_subject,
        message,
        SERVICE_EMAIL,
        [email],
        fail_silently=False
    )
    return Response(serializer.data, status=status.HTTP_200_OK)
