# Generated by Django 4.1.7 on 2023-05-29 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0014_doctor_dimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='dimage',
        ),
    ]
