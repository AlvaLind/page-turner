from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_request, name='book_request'),
]
