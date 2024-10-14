from django.shortcuts import render
# app/results/views.py
from rest_framework import viewsets
from .models import DivisionClassification, Examination, Result
from .serializers import DivisionClassificationSerializer, ExaminationSerializer, ResultSerializer

class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class DivisionClassificationViewSet(viewsets.ModelViewSet):
    queryset = DivisionClassification.objects.all()
    serializer_class = DivisionClassificationSerializer
