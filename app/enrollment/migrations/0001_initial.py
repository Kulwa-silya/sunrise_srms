# Generated by Django 4.2 on 2024-10-13 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_number', models.CharField(max_length=20, unique=True)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('current_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.form')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.specialization')),
            ],
        ),
    ]
