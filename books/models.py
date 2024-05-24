import uuid
from django.db import models


# Create your models here.


class Genre(models.Model):
    # Fields
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    class Meta: 
        ordering =["-name"]
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    # Relationships
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    published_year = models.IntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering =["-created_on"]
    
    def __str__(self):
        return self.title
    

    