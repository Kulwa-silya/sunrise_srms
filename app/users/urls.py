# app/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ParentProfileViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'parents', ParentProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
