from book.forms import BookForm
from book.models import Book
from django.shortcuts import render
# Create your views here.
def book_create(request):
    if request.method == 'POST':
        pass
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})