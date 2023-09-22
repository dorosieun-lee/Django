from django.contrib import admin
from .models import Article

# Register your models here.

# Article 모델 클래스를 admin site에 등록
admin.site.register(Article)
