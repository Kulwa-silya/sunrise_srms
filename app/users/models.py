#app/users/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(_('phone number'), max_length=10, unique=True)
    email = models.EmailField(_('email address'), blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

class ParentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    children = models.ManyToManyField('enrollment.Student', related_name='parents')

    def __str__(self):
        return f"Parent: {self.user.get_full_name()}"

class TeacherRole(models.Model):
    ROLE_CHOICES = [
        ('ACADEMIC', 'Academic Teacher'),
        ('DISCIPLINE', 'Discipline Teacher'),
        ('PATRON', 'Patron'),
        ('MATRON', 'Matron'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_role_display()

class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey('core.Department', on_delete=models.SET_NULL, null=True, blank=True)
    additional_roles = models.ManyToManyField(TeacherRole, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - Teacher"

class StaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    department = models.ForeignKey('core.Department', on_delete=models.SET_NULL, null=True, blank=True)
    additional_roles = models.ManyToManyField(TeacherRole, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {'Teacher' if self.is_teacher else 'Staff'}"
