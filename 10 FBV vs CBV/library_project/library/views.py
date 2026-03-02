from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books':books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book':book})

def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title = title,
            author = author,
            price = price)
        return redirect('fbv_book_list')
    return render(request, 'library/book_form.html')

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.price = request.POST.get("price")
        book.save()

        return redirect("fbv_book_list")

    return render(request, "library/book_update.html", {"book": book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("fbv_book_list")

    return render(request, "library/book_confirm_delete.html", {"book": book})

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'

    
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'price']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('cbv_book_list')

from django.views.generic import UpdateView, DeleteView

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'price']
    template_name = "library/book_update.html"
    success_url = reverse_lazy("cbv_book_list")

class BookDeleteView(DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("cbv_book_list")