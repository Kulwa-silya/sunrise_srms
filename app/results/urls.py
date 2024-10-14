# app/results/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DivisionClassificationViewSet, ExaminationViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'examinations', ExaminationViewSet)
router.register(r'results', ResultViewSet)
router.register(r'divisions', DivisionClassificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
