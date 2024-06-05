from django import forms
from .models import Comment, Rating


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a book 
    """
    class Meta:
        """
        Specify the Comment model and order of the fields
        """
        model = Comment
        fields = ('body',)
        

choices = [
    (1, 'One Star'),
    (2, 'Two Stars'),
    (3, 'Three Stars'),
    (4, 'Four Stars'),
    (5, 'Five Stars')
]
class RatingForm(forms.ModelForm):
    """
    Form class for users to rate a book
    RadioSelect widget renders the choices as star icons (radio buttons) 
    """
    rating = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    
    class Meta:
        """
        Specify the Rating model and order of the fields.  
        """
        model = Rating
        fields = ('rating',)