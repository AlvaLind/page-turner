from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book



# Create your views here.
class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "book_list.html"
    
def book_detail(request, slug):
    """
    Display an individual :model:'books.Book'.
    
    **Context**
    
    ''book''
        An instance of :model:'books.Book'.
        
    **Template:**
    
    :template:'books/book_detail.html'
    """
    
    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)
    
    return render(request, "books/book_detail.html", {"book": book},)