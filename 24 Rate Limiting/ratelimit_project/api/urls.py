from django.urls import path
from .views import message_list, limited_view, ExampleView

urlpatterns = [
    path('messages/', message_list),
    path('limit/', limited_view),
    path('example/', ExampleView.as_view()),
]