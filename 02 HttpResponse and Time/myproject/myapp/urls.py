from django.urls import path
from .views import display, my_view

urlpatterns = [
    path('display/', display, name='display'),
    path('my_view/',my_view , name='my_view'),
]
