# app/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeacherProfileViewSet,
    ParentProfileViewSet,
    StaffProfileViewSet
)

router = DefaultRouter()
router.register(r'teacher-profiles', TeacherProfileViewSet)
router.register(r'parent-profiles', ParentProfileViewSet)
router.register(r'staff-profiles', StaffProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
