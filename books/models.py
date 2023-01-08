from django.db import models
from django.utils import timezone
import datetime


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published', blank=True)
    created_date = models.DateTimeField(
        'date created', auto_now_add=True, blank=True)
    writer = models.ForeignKey(
        'Author', verbose_name="book author", on_delete=models.CASCADE, related_name="related_author")
    published_by = models.ForeignKey(
        'Publisher', verbose_name="book publisher", on_delete=models.CASCADE, related_name='related_publisher')

    def __str__(self) -> str:
        return self.book_name


class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_bio = models.CharField(
        max_length=500, blank=True, verbose_name='Author Biography')

    class Meta:
        ordering = ['author_name']

    def __str__(self) -> str:
        return self.author_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)
    publisher_address = models.CharField(
        max_length=200, blank=True, verbose_name='Publisher Address')

    # published_authors = models.ManyToManyField(
    #     "Author", verbose_name="Published Authors", through="Book")
    # published_books = models.ManyToManyField(
    #     "Book", verbose_name="Published Books")

    class Meta:
        ordering = ['publisher_name']

    def __str__(self) -> str:
        return self.publisher_name


# Create your models here.
