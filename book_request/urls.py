from django.urls import path
from . import views

urlpatterns = [
    path('/book_request', views.book_request, name='book_request'),
]