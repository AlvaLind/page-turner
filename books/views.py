from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Book
from .forms import CommentForm



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
    
    comments = book.comments.all().order_by("-created_on")
    comment_count = book.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted and is awaiting approval'
            )
            
    comment_form = CommentForm() # Empty the comment form.
    
    return render(request, "books/book_detail.html", {
        "book": book,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,       
        },
    )