from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    s = "<h1>Hello students, Welcome to Django Class!! </h1>"
    return HttpResponse(s)


def my_view(request):
    return HttpResponse("Hello Students!, Welcome to Django World!")