from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import Book, Comment, Rating 
from .forms import CommentForm, RatingForm



# Create your views here.
class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "book_list.html"
    paginate_by = 9
    
def book_detail(request, slug):
    """
    Display an individual :model:'books.Book'.
    
    **Context**
    
    ''book''
        An instance of :model:'books.Book'.
    ''comments''
        All comments related to the book.
    ''comment_count''
        Total count of admin approved comments related to the book.
    ''comment_form''
        An instance of :form:'books.CommentForm'.
    ''rating_form''
        An instance of :form:'books.RatingForm'.
        
    **Template:**
    
    :template:'books/book_detail.html'
    """
    
    # Retrieve the book 
    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)    
    
    # Retrieve comments 
    comments = book.comments.all().order_by("-created_on")
    comment_count = book.comments.filter(approved=True).count()
    
    # Handle the comment form submission
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
            print("Comment submitted successfully")
            return HttpResponseRedirect(reverse('book_detail', args=[slug]))
    else:
        # Empty the comment form        
        comment_form = CommentForm()
    
    # Handle the rating form submission
    if request.method == "POST":    
        rating_form = RatingForm(data=request.POST)
       
        if rating_form.is_valid():
            rating_value = rating_form.cleaned_data['rating']
            # Get or create a rating object for the user and book
            rating, created = Rating.objects.get_or_create(user=request.user, book=book)
            rating.rating = rating_value
            rating.save()
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Rating submitted successfully', 'user_rating': rating_value})
            return HttpResponseRedirect(reverse('book_detail', args=[slug]))

    else:
        # Empty the rating form  
        rating_form = RatingForm()
    
    # Retreive the user's rating for the book
    user_rating = None
    if request.user.is_authenticated:
        user_rating_obj = Rating.objects.filter(book=book, user=request.user).first()
        if user_rating_obj:
            user_rating = user_rating_obj.rating
    print("users rating is now:", user_rating)   
     
    # Pass variables to the book_detail template            
    return render(request, "books/book_detail.html", {
        "book": book,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "rating_form": rating_form,  
        "user_rating": user_rating,     
        },
    )
    

def comment_edit(request, slug, comment_id):
    """
    Edit an individual comment related to a book.

    **Context**

    ``book``
        An instance of :model:`books.Book`.
    ``comment``
        A single comment related to the book.
    ``comment_form``
        An instance of :form:`books.CommentForm`.
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
            print("Comment edited successfully")
        else:
            messages.add_message(request, messages.ERROR, 'Error, unable to update comment!')
            print("Error: Comment edit failed")

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment related to a book.

    **Context**

    ``book``
        An instance of :model:`books.Book`.
    ``comment``
        A single comment related to the book.
    """
    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
        print("Comment deleted successfully")
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
        print("Error: Comment delete failed - not users comment")

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


