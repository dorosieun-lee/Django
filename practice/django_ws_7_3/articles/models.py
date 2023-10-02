from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(source='image', 
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG',
                                     options= {'quality': 90}) 
    