from django.urls import path
from . import views

urlpatterns = [
    path('fbv/books/', views.book_list, name='fbv_book_list'),
    path('fbv/books/<int:pk>/', views.book_detail, name='fbv_book_detail'),
    path('fbv/books/add/', views.book_create, name='fbv_book_create'),
    path('fbv/books/<int:pk>/update/', views.book_update, name='fbv_book_update'),
    path('fbv/books/<int:pk>/delete/', views.book_delete, name='fbv_book_delete'),

    path('cbv/books/', views.BookListView.as_view(), name='cbv_book_list'),
    path('cbv/books/<int:pk>/', views.BookDetailView.as_view(), name='cbv_book_detail'),
    path('cbv/books/add/', views.BookCreateView.as_view(), name='cbv_book_create'),
    path('cbv/books/<int:pk>/update/', views.BookUpdateView.as_view(),
     name='cbv_book_update'),

    path('cbv/books/<int:pk>/delete/', views.BookDeleteView.as_view(),
     name='cbv_book_delete'),
]