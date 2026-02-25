from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books'),
    path('dashboard/', views.sales_dashboard, name='dashboard'),
    path('raw/', views.raw_sql_view, name='raw'),
]