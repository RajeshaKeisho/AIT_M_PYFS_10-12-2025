from django.shortcuts import render
from .models import *
from django.db.models import Sum, F
from django.db.models import Count

from django.db import connection
# Create your views here.

def book_list(request):
    books = Book.objects.select_related('author')
    return render(request, 'books.html', {'books':books})

def sales_dashboard(request):
    books = Book.objects.annotate(total_sold = Sum('orderitem__quantity'))
    return render(request, 'dashboard.html', {'books':books})

def raw_sql_view(request):
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT title, price FROM store_book
""") 
        
        rows = cursor.fetchall()
    return render(request, 'raw.html', {'rows':rows})



def author_list(request):
    authors = Author.objects.annotate(
        total_books=Count('book')
    )

    return render(request, 'authors.html', {'authors': authors})

def author_list(request):
    authors = Author.objects.annotate(
        total_books=Count('book')
    )

    return render(request, 'authors.html', {'authors': authors})

def book_detail(request, book_id):
    book = Book.objects.select_related('author').get(id=book_id)
    orders = OrderItem.objects.filter(book=book)

    context = {
        'book': book,
        'orders': orders
    }

    return render(request, 'book_detail.html', context)

def customer_orders(request):
    customers = Customer.objects.prefetch_related(
        'order_set'
    )

    return render(request, 'customers.html', {'customers': customers})

def low_stock(request):
    books = Book.objects.filter(stock__lt=20).order_by('stock')
    return render(request, 'low_stock.html', {'books': books})

from django.db.models import Sum

def customer_summary(request):
    customers = Customer.objects.annotate(
        total_items=Sum('order__orderitem__quantity')
    )

    return render(request, 'customer_summary.html', {'customers': customers})

def search_books(request):
    query = request.GET.get('q')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    return render(request, 'search.html', {
        'books': books,
        'query': query
    })


def top_books(request):
    books = Book.objects.annotate(
        total_sold=Sum('orderitem__quantity')
    ).order_by('-total_sold')[:5]

    return render(request, 'top_books.html', {'books': books})