from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserProfileForm
from books.models import Bookshelf, Book

# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':
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
    
    bookshelf = Bookshelf.objects.filter(user=request.user)
    books_in_bookshelf = Book.objects.filter(bookshelf__in=bookshelf)

    
    
    return render(request, 'profile_page.html', {'form': form, 'bookshelf': bookshelf, 'books_in_bookshelf': books_in_bookshelf,})
