#app/results/models.py
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

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
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]

    student = models.ForeignKey('enrollment.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('core.Subject', on_delete=models.CASCADE)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    points = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    uploaded_by = models.ForeignKey('users.TeacherProfile', on_delete=models.SET_NULL, null=True, related_name='results_uploaded')
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey('users.TeacherProfile', on_delete=models.SET_NULL, null=True, related_name='results_approved')

    class Meta:
        unique_together = ('student', 'subject', 'examination')

    def save(self, *args, **kwargs):
        self.grade = self.calculate_grade()
        self.points = self.calculate_points()
        super().save(*args, **kwargs)

    def calculate_grade(self):
        if self.marks >= 75:
            return 'A'
        elif self.marks >= 65:
            return 'B'
        elif self.marks >= 45:
            return 'C'
        elif self.marks >= 30:
            return 'D'
        else:
            return 'F'

    def calculate_points(self):
        grade_points = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5}
        return grade_points[self.grade]

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.examination}"


class DivisionClassification(models.Model):
    DIVISION_CHOICES = [
        ('I', 'Division I'),
        ('II', 'Division II'),
        ('III', 'Division III'),
        ('IV', 'Division IV'),
        ('0', 'Fail'),
    ]

    student = models.ForeignKey('enrollment.Student', on_delete=models.CASCADE)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    total_points = models.IntegerField()
    division = models.CharField(max_length=3, choices=DIVISION_CHOICES)

    class Meta:
        unique_together = ('student', 'examination')

    def save(self, *args, **kwargs):
        self.division = self.calculate_division()
        super().save(*args, **kwargs)

    def calculate_division(self):
        if self.total_points <= 17:
            return 'I'
        elif self.total_points <= 21:
            return 'II'
        elif self.total_points <= 25:
            return 'III'
        elif self.total_points <= 33:
            return 'IV'
        else:
            return '0'

    def __str__(self):
        return f"{self.student} - {self.examination} - Division {self.division}"
