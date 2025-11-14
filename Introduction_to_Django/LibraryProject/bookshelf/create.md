# Create Operation

>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984 by George Orwell (1949)>

# Expected Output:
A new Book instance is successfully created with the given title, author, and publication year.
# Create Operation
