# app/enrollment/serializers.py
from rest_framework import serializers
from .models import Student, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'current_form', 'specialization', 'enrollment_number', 'date_of_birth', 'address']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'class_assigned', 'academic_year']
