# Generated by Django 4.2 on 2024-10-13 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enrollment', '0002_initial'),
        ('core', '0002_initial'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='results_approved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.examination'),
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment.student'),
        ),
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject'),
        ),
        migrations.AddField(
            model_name='result',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='results_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='divisionclassification',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.examination'),
        ),
        migrations.AddField(
            model_name='divisionclassification',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment.student'),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('student', 'subject', 'examination')},
        ),
        migrations.AlterUniqueTogether(
            name='divisionclassification',
            unique_together={('student', 'examination')},
        ),
    ]
