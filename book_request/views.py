from django.shortcuts import render
from django.contrib import messages
from .forms import BookRequestForm
from .models import BookRequest

def book_request(request):
    """
    Renders a form for users to be able to request
    a new book they want to see on the site
    
    Displays an individual instance of :model:`book_request.BookRequest`.
    
    **Context**
    ``book_request``
        The most recent instance of :model:`book_request.BookRequest`.
        ``BookRequest form``
        
    **Template**
    :template:'book_request/book_request.html'
    """
    if request.method == "POST":
        bookRequest_form = BookRequestForm(data=request.POST)
        if bookRequest_form.is_valid():
            bookRequest_form.save()
            messages.add_message(request, messages.SUCCESS, "Thankyou for your book recommendation!")
            
    bookRequest_form = BookRequestForm()
    
    return render(request, "book_request/book_request.html", {"bookRequest_form": bookRequest_form},)