# Generated by Django 5.1.2 on 2024-11-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0002_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.TextField(max_length=10, null=True),
        ),
    ]
