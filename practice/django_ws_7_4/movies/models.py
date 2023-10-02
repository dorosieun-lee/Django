from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    synopsis = models.TextField()
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(source='image', 
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG',
                                     options= {'quality': 90}) 
    