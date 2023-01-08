# Generated by Django 4.1.5 on 2023-01-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_publisher_published_authors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_bio',
            field=models.CharField(blank=True, max_length=500, verbose_name='Author Biography'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='publisher_address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Publisher Address'),
        ),
    ]