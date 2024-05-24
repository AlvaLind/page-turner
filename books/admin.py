from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'author', 'genre', 'published_year',)
    search_fields = ['title', 'author', 'genre']
    list_filter = ('genre', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    
    
# Register your models here.