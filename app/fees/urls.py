# app/fees/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeeViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'fees', FeeViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
