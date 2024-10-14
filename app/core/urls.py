# app/core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, DepartmentViewSet, EventViewSet, FormViewSet, NotificationViewSet, SpecializationViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'events', EventViewSet)
router.register(r'forms', FormViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'specializations', SpecializationViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
