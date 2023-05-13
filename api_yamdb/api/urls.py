from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TitleViewSet,
                    CategoryViewSet,
                    GenreViewSet,
                    UserViewSet,
                    get_token,
                    get_confirmation_code)

router = DefaultRouter()
router.register('titles', TitleViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/auth/signup/', get_confirmation_code,
         name='get_confirmation_code'),
]
