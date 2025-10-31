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

def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'book/book_list.html', {'books':books})

def book_detail (request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book/book_details.html', {'book':book})

def book_update (request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request. POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success (request, 'Book updatedsuccessfully!')
            return redirect('book-update', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render (request, 'book/book_form.html', {'form': form})

def book_delete (request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success (request, 'Book deleted successfully!')
    return redirect('book-list')