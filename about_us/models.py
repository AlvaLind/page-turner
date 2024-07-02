from django.db import models
from cloudinary.models import CloudinaryField


class About_Us(models.Model):
    title = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
