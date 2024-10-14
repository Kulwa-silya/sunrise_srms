# app/core/views.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Class, Department, Event, Form, Notification, Specialization, Subject
from .serializers import ClassSerializer, DepartmentSerializer, EventSerializer, FormSerializer, NotificationSerializer, SpecializationSerializer, SubjectSerializer
from .permissions import IsTeacherOrReadOnly, IsSubjectTeacher

# class ClassViewSet(viewsets.ModelViewSet):
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacherprofile'):
            return Class.objects.filter(teachers=user.teacherprofile)
        return Class.objects.none()

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

# class SubjectViewSet(viewsets.ModelViewSet):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacherprofile'):
            return Subject.objects.filter(teachers=user.teacherprofile)
        return Subject.objects.none()
