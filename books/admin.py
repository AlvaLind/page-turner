from django.contrib import admin
from .models import Book, Genre, Author
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Genre)
class GenreAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    and rich-text editor.
    """
    list_display = ('name',)
    search_fields = ['name', 'description']
    summernote_fields = ('description',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin and fields for search.
    """
    list_display = ('name', 'nationality', 'birth_date')
    search_fields = ['name']
    
    
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'author', 'genre', 'published_year',)
    search_fields = ['title', 'author', 'genre', 'description']
    list_filter = ('genre', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    
    
# Register your models here.
