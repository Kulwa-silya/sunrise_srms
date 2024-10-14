from django.shortcuts import render

# app/users/views.py
from rest_framework import viewsets
from .models import CustomUser, ParentProfile
from .serializers import CustomUserSerializer, ParentProfileSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ParentProfileViewSet(viewsets.ModelViewSet):
    queryset = ParentProfile.objects.all()
    serializer_class = ParentProfileSerializer
