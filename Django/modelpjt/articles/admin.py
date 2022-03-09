from django.contrib import admin
from .models import Article

# Register your models here. 
# admin site에서 사용할 model 등록

admin.site.register(Article)