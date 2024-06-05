import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.


class Genre(models.Model):
    # Fields
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    class Meta: 
        ordering =["name"]
    
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    
    class Meta: 
        ordering =["name"]
        
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    # Relationships
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    published_year = models.IntegerField()
    cover_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering =["-published_year"]
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:'auth.User'
    and :model:'books/Book'.
    """    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(max_length=1000)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
       return f"Comment {self.body} by {self.user}"
        

class Rating(models.Model):
    """
    Stores a single rating entry related to :model:'auth.User'
    and :model:'books/Book'.
    
    Each user can rate each book only once. The rating is an integer
    value between 1 and 5 inclusive.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rater")
    rating = models.IntegerField(choices=[(i, i) for i in range (1, 6)], blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    """
    Enforces uniqueness constraints on the fields user and book in the model.
    This means the combination of the user and book values must be unique and not already exist. 
    It will make sure a user can rate a particular book only once. 
    """
    class Meta:
        unique_together = ('user', 'book') 
        
    def __str__(self):
        return f'{self.book.title} - {self.rating} stars {self.user.username}'