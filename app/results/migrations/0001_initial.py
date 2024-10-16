# Generated by Django 4.2 on 2024-10-13 23:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DivisionClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.IntegerField()),
                ('division', models.CharField(choices=[('I', 'Division I'), ('II', 'Division II'), ('III', 'Division III'), ('IV', 'Division IV'), ('0', 'Fail')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exam_type', models.CharField(choices=[('REGULAR', 'Regular Assessment'), ('MOCK', 'Mock Exam'), ('NECTA', 'National Exam (NECTA)')], max_length=10)),
                ('date', models.DateField()),
                ('term', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('points', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
