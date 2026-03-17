# from django.shortcuts import render
from rest_framework import generics, pagination
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page-size"
    max_page_size = 100


class BookLimitOffSetPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'my_limit'
    offset_query_param = 'my_offset'
    max_limit = 100

class BookCursorPagination(pagination.CursorPagination):
    page_size = 10
    ordering = 'title'

class BookListViewPageNumber(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPageNumberPagination

class BookListViewLimitOffSet(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookLimitOffSetPagination

class BookListViewCursor(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookCursorPagination