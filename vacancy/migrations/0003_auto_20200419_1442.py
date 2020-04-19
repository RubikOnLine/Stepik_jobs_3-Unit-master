# Generated by Django 3.0.4 on 2020-04-19 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_auto_20200419_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_speciality', to='vacancy.Speciality'),
        ),
    ]