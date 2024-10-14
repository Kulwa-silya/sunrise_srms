# app/core/permissions.py
from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(request.user, 'teacherprofile')

class IsSubjectTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'teacherprofile'):
            return request.user.teacherprofile in obj.teachers.all()
        return False

class IsStaffOrTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'staffprofile')

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'teacherprofile')

class IsParentOfStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'parentprofile'):
            return obj.student in request.user.parentprofile.children.all()
        return False
