from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TitleViewSet,
                    CategoryViewSet,
                    GenreViewSet,
                    UserViewSet,
                    get_token,
                    get_confirmation_code,
                    ReviewViewSet,
                    CommentViewSet)

router = DefaultRouter()
router.register('titles', TitleViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('users', UserViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/auth/signup/', get_confirmation_code,
         name='get_confirmation_code'),
]
