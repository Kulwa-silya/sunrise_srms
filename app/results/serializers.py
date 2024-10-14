# app/results/serializers.py
from rest_framework import serializers
from .models import DivisionClassification, Examination, Result
from app.users.serializers import TeacherProfileSerializer


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ['id', 'name', 'exam_type', 'date', 'term', 'year']

# class ResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Result
#         fields = ['id', 'student', 'subject', 'examination', 'marks', 'grade', 'points', 'uploaded_by', 'approved', 'approved_by']

class ResultSerializer(serializers.ModelSerializer):
    uploaded_by = TeacherProfileSerializer(read_only=True)
    approved_by = TeacherProfileSerializer(read_only=True)
    student = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    examination = serializers.StringRelatedField()

    class Meta:
        model = Result
        fields = ['id', 'student', 'subject', 'examination', 'marks', 'grade', 'points', 'uploaded_by', 'approved', 'approved_by']
        read_only_fields = ['grade', 'points', 'approved', 'approved_by']


class DivisionClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionClassification
        fields = ['id', 'student', 'examination', 'total_points', 'division']
