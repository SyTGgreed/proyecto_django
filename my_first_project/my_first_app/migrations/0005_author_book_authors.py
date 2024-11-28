# Generated by Django 5.1.2 on 2024-11-28 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0004_publisher_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('birth_day', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='my_first_app.author'),
        ),
    ]
