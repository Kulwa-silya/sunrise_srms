from django.db import models
from django.conf import settings
from app.core.models import Form, Specialization, Class

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_form = models.ForeignKey(Form, on_delete=models.SET_NULL, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True)
    enrollment_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.enrollment_number}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True)
    academic_year = models.CharField(max_length=9)  # e.g., "2023/2024"
    class_assigned = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student} - {self.form} - {self.academic_year}"
