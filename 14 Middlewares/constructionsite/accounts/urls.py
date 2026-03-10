from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('under_construction/', views.under_construction, name='under_construction'),
    path('test-exception/', views.test_exception_view, name='test_exception'),
]