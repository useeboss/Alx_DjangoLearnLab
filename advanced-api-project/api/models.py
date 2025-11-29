from django.db import models
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

class Author(models.Model):
    """
    Represents an author entity.
    Each author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book entity.
    Each book is linked to a single author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"



# Create author and book
author = Author.objects.create(name="Chinua Achebe")
book = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=author)

# Serialize
serializer = AuthorSerializer(author)
print(serializer.data)
# Output: {'id': 1, 'name': 'Chinua Achebe', 'books': [{'id': 1, 'title': 'Things Fall Apart', 'publication_year': 1958, 'author': 1}]}
