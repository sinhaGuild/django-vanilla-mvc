from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Author, Book, Publisher


def index(request):
    latest_books = Book.objects.all()
    context = {'latest_books': latest_books}
    # return JsonResponse({'status': "success", 'allBooks': latest_books})
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'books/detail.html', {'book': book})


def authors(request, author_id):
    try:
        # books_by_author = Author.objects.filter(pk=author_id)
        retieved_author = Author.objects.get(id=author_id)
        books_by_author = Book.objects.filter(writer_id=author_id)
    except Author.DoesNotExist:
        raise Http404("Author-Relationship does not exist")
    return render(request, 'books/author.html', {"books_by_author": books_by_author, "author": retieved_author})


def publishers(request, publisher_id):
    try:
        # books_by_author = Author.objects.filter(pk=author_id)
        retieved_publisher = Publisher.objects.get(id=publisher_id)
        books_by_publisher = Book.objects.filter(published_by_id=publisher_id)
    except Publisher.DoesNotExist:
        raise Http404("Publisher-Relationship does not exist")
    return render(request, 'books/publishers.html', {"books_by_publisher": books_by_publisher, "publisher": retieved_publisher})

# Create your views here.
