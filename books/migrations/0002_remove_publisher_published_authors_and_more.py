# Generated by Django 4.1.5 on 2023-01-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='published_authors',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='published_books',
        ),
    ]