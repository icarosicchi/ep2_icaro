# Generated by Django 4.2.7 on 2023-11-13 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='author',
        ),
    ]
