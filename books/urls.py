from . import views
from django.urls import path

urlpatterns = [
     path('', views.Homepage, name='homepage'),
     path('books/', views.BookList.as_view(), name='books'),
     path('books/<slug:slug>/', views.book_detail, name='book_detail'),
     path('books/<slug:slug>/comment/edit/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('books/<slug:slug>/comment/delete/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('search/', views.search_books, name='search_books'),
]