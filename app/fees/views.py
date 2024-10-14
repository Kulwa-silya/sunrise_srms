# app/fees/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Fee, Transaction
from .serializers import FeeSerializer, TransactionSerializer

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
