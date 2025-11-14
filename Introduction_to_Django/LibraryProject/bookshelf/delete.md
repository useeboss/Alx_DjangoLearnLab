# Delete Operation

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})

>>> Book.objects.all()
<QuerySet []>

# Expected Output:
The Book instance is successfully deleted. Retrieving all books confirms the database is empty.
# Delete Operation
