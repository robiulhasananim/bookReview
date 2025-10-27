from book.forms import BookForm
from book.models import Book
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success (request, 'Book created successfully!')
            return redirect('book-create')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})