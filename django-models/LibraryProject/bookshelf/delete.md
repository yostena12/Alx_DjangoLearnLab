from bookshelf.models import Book

# Retrieve all books before deletion
Book.objects.all()
# Expected output: <QuerySet [<Book: 1984>]>

# Get the book instance
book = Book.objects.get(title="1984")

# Delete the book
book.delete()
# Expected output: (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Expected output: <QuerySet []>
