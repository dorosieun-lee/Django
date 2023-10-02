from django.contrib import admin
from .models import Book

# Register your models here.
class Layout_Book(admin.ModelAdmin):
  list_display = ('isbn','title','author','publisher','pubdate','description','price','adult','rank')
admin.site.register(Book, Layout_Book)
