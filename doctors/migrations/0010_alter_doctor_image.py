# Generated by Django 4.1.7 on 2023-05-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0009_remove_doctor_institution_alter_doctor_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
