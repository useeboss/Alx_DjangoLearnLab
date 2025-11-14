# Update Operation

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
<Book: Nineteen Eighty-Four by George Orwell (1949)>

# Expected Output:
The Book instance is successfully updated with the new title "Nineteen Eighty-Four".
# Update Operation
