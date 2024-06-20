from .models import BookRequest
from django import forms

class BookRequest(forms.ModelForm):
    """
    Form class for users to request a book
    to be added to the site
    """
    class Meta:
        """
        Specify the book request model and order the fields 
        """
        model = BookRequest
        fields = ('title', 'author', 'published_year', 'description', 'cover_image',)