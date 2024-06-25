from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from .models import Book, Comment, Rating, Bookshelf
from .forms import CommentForm, RatingForm, BookSearchForm

# Create your views here.
class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "book_list.html"
    paginate_by = 9
    
    
def Homepage(request):
    latest_books = Book.objects.order_by('-created_on')[:6] # Most recently added 6 books
    context = {'book_list': latest_books}
    return render(request, 'homepage.html', context)


def search_books(request):
    """
    Search for books by title, author, or genre.
    
    **Context**
    
    ''form''
        An instance of :form:'books.BookSearchForm'.
    ''books''
        A queryset containing all books that match the search query.
        
    **Template:**
    
    :template:'books/search_books.html'
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    query = None
    
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            books = books.filter(
                Q(title__icontains=query) | 
                Q(author__name__icontains=query) | 
                Q(genre__name__icontains=query)
            )
    
    return render(request, 'search_books.html', {'form': form, 'query': query, 'book_list': books})
    
    
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
    
    # Retrieve all ratings for this book 
    book_ratings = Rating.objects.filter(book=book).exclude(rating=-1).values_list('rating', flat=True)
    # Calculate total number of ratings left on the book
    total_ratings = Rating.objects.filter(book=book).count()
    
    # Calculate average rating
    if book_ratings:
        average_rating = sum(book_ratings) / len(book_ratings)
    else:
        average_rating = None 
        
    # Handle the rating form submission
    if request.method == "POST":    
        rating_form = RatingForm(data=request.POST)
       
        if rating_form.is_valid():
            rating_value = rating_form.cleaned_data['rating']
            # Get or create a rating object for the user and book
            rating, created = Rating.objects.get_or_create(user=request.user, book=book)
            rating.rating = rating_value
            rating.save()
            print("Rating submitted successfully")
            
            # Calculate the average book rating
            book_ratings = Rating.objects.filter(book=book).exclude(rating=-1).values_list('rating', flat=True)
            if book_ratings:
                average_rating = sum(book_ratings) / len(book_ratings)
                total_ratings = Rating.objects.filter(book=book).count()
            else:
                average_rating = None 
        
            # Check if request was made using AJAX and return a JSON response back to ratings.js submitForm function to be processed. 
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Rating submitted successfully', 
                                     'user_rating': rating_value, 
                                     'average_rating': average_rating, 
                                     'total_ratings': total_ratings,
                                     })
            
            # If not an AJAX request, respond with a HTTP response to redirect user to book detail page
            return HttpResponseRedirect(reverse('book_detail', args=[slug]))

    else:
        # Empty the rating form  
        rating_form = RatingForm()
    
    user_rating = None
    # Retrieve the user's rating for the book if the user is authenticated
    if request.user.is_authenticated:
        user_rating_obj = Rating.objects.filter(book=book, user=request.user).first()
        if user_rating_obj:
            user_rating = user_rating_obj.rating

    # Pass variables to the book_detail template            
    return render(request, "books/book_detail.html", {
        "book": book,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "rating_form": rating_form,  
        "user_rating": user_rating,
        "average_rating": average_rating, 
        "total_ratings": total_ratings,
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

# Add and remove books from bookshelf
@login_required
def add_to_bookshelf(request, slug):
    book = get_object_or_404(Book, slug=slug)
    bookshelf_entry, created = Bookshelf.objects.get_or_create(user=request.user, book=book)
    if created:
        bookshelf_entry.status = 'unread'  # default status
        bookshelf_entry.save()
    messages.add_message(request, messages.SUCCESS, 'This book has been added to your Bookshelf!')
    
    return redirect('book_detail', slug=slug)
    

@login_required
def remove_from_bookshelf(request, slug):
    book = get_object_or_404(Book, slug=slug)
    bookshelf_entry = get_object_or_404(Bookshelf, user=request.user, book=book)
    bookshelf_entry.delete()
    messages.add_message(request, messages.SUCCESS, 'This book has been removed from your Bookshelf!')

    return redirect('book_detail', slug=slug)

