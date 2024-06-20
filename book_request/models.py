from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class BookRequest(models.model):
    """
    Stores a single Book request message.
    For users to request a book to be added to the site
    """
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    published_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    cover_image = CloudinaryField('image', default='placeholder')
    read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requester")
    
    def __str__(self):
        return f"{self.user} has requested the book: {self.title}"