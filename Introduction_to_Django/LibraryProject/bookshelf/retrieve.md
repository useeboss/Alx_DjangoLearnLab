# Retrieve Operation

>>> from bookshelf.models import Book
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

>>> Book.objects.get(title="1984")
<Book: 1984 by George Orwell (1949)>

# Expected Output:
The Book instance created earlier is successfully retrieved and its details are displayed.
# Retrieve Operation
