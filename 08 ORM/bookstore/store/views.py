from django.shortcuts import render
from .models import *
from django.db.models import Sum, F
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
