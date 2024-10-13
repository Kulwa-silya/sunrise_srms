from django.db import models
from django.conf import settings

class Form(models.Model):
    name = models.CharField(max_length=10)
    level = models.IntegerField(choices=[(i, f"Form {i}") for i in range(1, 5)])

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    CATEGORY_CHOICES = [
        ('CORE', 'Core'),
        ('BUSINESS', 'Business'),
        ('SCIENCE', 'Science'),
    ]
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subjects_taught')
    forms = models.ManyToManyField(Form)
    specializations = models.ManyToManyField(Specialization, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"



class Department(models.Model):
    # ... (existing fields)

class Class(models.Model):
    name = models.CharField(max_length=50)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.IntegerField()
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='classes_taught')

    def __str__(self):
        return f"{self.name} - {self.form} - {self.year}"


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('GRADUATION', 'Graduation'),
        ('EXAM', 'Exam'),
        ('MEETING', 'Meeting'),
        ('HOLIDAY', 'Holiday'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events')
    is_mandatory = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.start_datetime}"

class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('EVENT', 'Event Reminder'),
        ('ANNOUNCEMENT', 'Announcement'),
    ]
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE_CHOICES)

    def __str__(self):
        return f"Notification for {self.recipient}: {self.message[:50]}..."
