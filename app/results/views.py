from django.shortcuts import render
# app/results/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import OR
from .models import DivisionClassification, Examination, Result
from .serializers import DivisionClassificationSerializer, ExaminationSerializer, ResultSerializer
from app.core.permissions import IsTeacher, IsSubjectTeacher, IsParentOfStudent


class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated, OR(IsTeacher, IsParentOfStudent)]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Result.objects.all()
        elif hasattr(user, 'teacherprofile'):
            return Result.objects.filter(subject__teachers=user.teacherprofile)
        elif hasattr(user, 'parentprofile'):
            return Result.objects.filter(student__in=user.parentprofile.children.all())
        elif hasattr(user, 'student'):
            return Result.objects.filter(student=user.student)
        return Result.objects.none()

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user.teacherprofile)

    def perform_update(self, serializer):
        if 'approved' in serializer.validated_data and serializer.validated_data['approved']:
            serializer.save(approved_by=self.request.user.teacherprofile)
        else:
            serializer.save()

class DivisionClassificationViewSet(viewsets.ModelViewSet):
    queryset = DivisionClassification.objects.all()
    serializer_class = DivisionClassificationSerializer
    permission_classes = [IsAuthenticated, OR(IsTeacher, IsParentOfStudent)]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or hasattr(user, 'teacherprofile'):
            return DivisionClassification.objects.all()
        elif hasattr(user, 'parentprofile'):
            return DivisionClassification.objects.filter(student__in=user.parentprofile.children.all())
        elif hasattr(user, 'student'):
            return DivisionClassification.objects.filter(student=user.student)
        return DivisionClassification.objects.none()
