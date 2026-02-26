from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books'),
    path('dashboard/', views.sales_dashboard, name='dashboard'),
    path('raw/', views.raw_sql_view, name='raw'),

    # NEW URLS
    path('authors/', views.author_list, name='authors'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('customers/', views.customer_orders, name='customers'),
    path('low-stock/', views.low_stock, name='low_stock'),
    path('customer-summary/', views.customer_summary, name='customer_summary'),
    path('search/', views.search_books, name='search_books'),
    path('top-books/', views.top_books, name='top_books'),
]