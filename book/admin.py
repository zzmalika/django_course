from django.contrib import admin

# Register your models here.
from book.models import Book, Author, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_date', 'author', 'publisher']
    ordering = ['title']
    search_fields = ['title', 'author__first_name', 'author__last_name']
    list_filter = ['publication_date', 'publisher']