from django.db import models
from django.conf import settings

class Examination(models.Model):
    EXAM_TYPE_CHOICES = [
        ('REGULAR', 'Regular Assessment'),
        ('MOCK', 'Mock Exam'),
        ('NECTA', 'National Exam (NECTA)'),
    ]
    name = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE_CHOICES)
    date = models.DateField()
    term = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.exam_type} ({self.date})"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='results_uploaded')
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='results_approved')

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.examination}"
