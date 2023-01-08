from django.contrib import admin
from .models import Author, Book, Publisher
from django.apps import apps


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['book_name']}),
        ('Date Information', {
            'fields': [
                'writer', 'published_by', 'published_date'],
            'description': ('Authorship')}),
    ]
    list_display = ('book_name', 'published_date',
                    'created_date', 'writer', 'published_by')


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)

# Register your models here.
