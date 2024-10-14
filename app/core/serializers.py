# app/core/serializers.py
from rest_framework import serializers
from .models import Class, Department, Event, Form, Notification, Specialization, Subject
from app.users.serializers import TeacherProfileSerializer

class ClassSerializer(serializers.ModelSerializer):
    teachers = TeacherProfileSerializer(many=True, read_only=True)
    form = serializers.StringRelatedField()
    specialization = serializers.StringRelatedField()

    class Meta:
        model = Class
        fields = ['id', 'name', 'form', 'specialization', 'academic_year', 'teachers']


class DepartmentSerializer(serializers.ModelSerializer):
    head = TeacherProfileSerializer(read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'head']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_type', 'start_datetime', 'end_datetime', 'location', 'created_by', 'participants', 'is_mandatory']

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'level']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'created_at', 'is_read', 'event', 'notification_type']

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name', 'description']

class SubjectSerializer(serializers.ModelSerializer):
    teachers = TeacherProfileSerializer(many=True, read_only=True)
    department = serializers.StringRelatedField()

    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'category', 'department', 'teachers', 'forms', 'specializations']
