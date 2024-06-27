from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserProfileForm
from books.models import Bookshelf, Book
from books.forms import BookshelfForm

@login_required
def profile(request):
    if request.method == 'POST' and 'profile_form' in request.POST:
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('new_password')
            if new_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)
            user.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(instance=request.user)
    
    if request.method == 'POST' and 'status_form' in request.POST:
        book_slug = request.POST.get('book_slug')
        status = request.POST.get('status')
        book = get_object_or_404(Book, slug=book_slug)
        bookshelf = get_object_or_404(Bookshelf, book=book, user=request.user)
        bookshelf.status = status
        bookshelf.save()
        return redirect('profile')
    
    bookshelf = Bookshelf.objects.filter(user=request.user)
    status_choices = Bookshelf.STATUS_CHOICES
    books_in_bookshelf = Book.objects.filter(bookshelf__in=bookshelf)
    

    # Prepare a list of dictionaries with book and status
    books_with_status = []
    for entry in bookshelf:
        books_with_status.append({
            'book': entry.book,
            'status': entry.get_status_display(),
        })
    
    return render(request, 'profile_page.html', {
        'form': form, 
        'bookshelf': bookshelf,
        'books_in_bookshelf': books_in_bookshelf,
        'books_with_status': books_with_status,
        'status_choices': status_choices,
    })
        
