from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Comment
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
    


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``book``
        An instance of :model:`blog.book`.
    ``comment``
        A single comment related to the book.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.book = book
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error, unable to update comment!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))