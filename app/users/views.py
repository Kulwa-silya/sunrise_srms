# app/users/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, TeacherProfile, ParentProfile, StaffProfile
from .serializers import (
    CustomUserSerializer,
    TeacherProfileSerializer,
    ParentProfileSerializer,
    StaffProfileSerializer
)
from app.core.permissions import IsTeacherOrReadOnly, IsStaffOrTeacher

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsStaffOrTeacher]

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAuthenticated, IsStaffOrTeacher]

class ParentProfileViewSet(viewsets.ModelViewSet):
    queryset = ParentProfile.objects.all()
    serializer_class = ParentProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or hasattr(user, 'teacherprofile'):
            return ParentProfile.objects.all()
        elif hasattr(user, 'parentprofile'):
            return ParentProfile.objects.filter(user=user)
        return ParentProfile.objects.none()

    def get_permissions(self):
        if self.action in ['list', 'create']:
            return [IsAuthenticated(), IsStaffOrTeacher()]
        return [IsAuthenticated()]

class StaffProfileViewSet(viewsets.ModelViewSet):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer
    permission_classes = [IsAuthenticated, IsStaffOrTeacher]
