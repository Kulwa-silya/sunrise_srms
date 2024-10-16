# Generated by Django 4.2 on 2024-10-13 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(related_name='subjects_taught', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.event'),
        ),
        migrations.AddField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headed_department', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='class',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.form'),
        ),
        migrations.AddField(
            model_name='class',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.specialization'),
        ),
        migrations.AddField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(related_name='classes_taught', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together={('name', 'form', 'specialization', 'academic_year')},
        ),
    ]
