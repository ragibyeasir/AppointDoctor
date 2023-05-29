# Generated by Django 4.1.7 on 2023-05-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_doctor_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='institution',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='study',
            field=models.CharField(choices=[('MBBS', 'MBBS'), ('BDS', 'BDS'), ('MD', 'MD'), ('FCPS', 'FCPS')], max_length=50),
        ),
    ]