from django.contrib import admin
from .models import Author, Book, Customer, Order, OrderItem
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)