from django.contrib import admin
from .models import Book

# Register the Book model with the admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right-hand side
    list_filter = ('author', 'publication_year')

    # Add a search bar for title and author
    search_fields = ('title', 'author')
