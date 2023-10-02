from django.db import models

# Create your models here.
class Book(models.Model):
  isbn = models.CharField(max_length=10)
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=50)
  publisher = models.CharField(max_length=50)
  pubdate = models.DateField()
  description = models.TextField()
  price = models.IntegerField()
  adult = models.BooleanField()
  rank = models.FloatField()

  def __str__(self):
    return f'제목 : {self.title}\n작가 : {self.author}\n별점: {self.rank}\n가격 : {self.price}'

  
