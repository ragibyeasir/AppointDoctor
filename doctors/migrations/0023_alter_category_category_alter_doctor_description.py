# Generated by Django 4.1.7 on 2023-05-30 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0022_alter_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.TextField(max_length=150, null=True),
        ),
    ]
