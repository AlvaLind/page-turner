from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]