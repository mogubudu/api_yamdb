from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import TitleViewSet, CategoryViewSet, GenreViewSet, UserViewSet

router = DefaultRouter()
router.register('titles', TitleViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
