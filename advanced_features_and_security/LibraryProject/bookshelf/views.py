from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .forms import SearchForm


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    # Only users with can_view can access
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    # Only users with can_create can access
    # Logic for creating a book
    pass

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    # Only users with can_edit can access
    pass

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    # Only users with can_delete can access
    pass



def book_search(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        query = form.cleaned_data["query"]
        # ✅ Safe ORM query (no string concatenation)
        results = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"form": form, "results": results})
