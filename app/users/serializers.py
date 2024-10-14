# app/users/serializers.py
from rest_framework import serializers
from .models import CustomUser, ParentProfile,TeacherProfile, StaffProfile, TeacherRole


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ParentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentProfile
        fields = ['id', 'user', 'children']

class TeacherRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherRole
        fields = ['id', 'role']

class TeacherProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    additional_roles = TeacherRoleSerializer(many=True, read_only=True)

    class Meta:
        model = TeacherProfile
        fields = ['id', 'user', 'department', 'additional_roles']

class StaffProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    additional_roles = TeacherRoleSerializer(many=True, read_only=True)

    class Meta:
        model = StaffProfile
        fields = ['id', 'user', 'is_teacher', 'department', 'additional_roles']
