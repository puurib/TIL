from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField() #제한없이 적음
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add 최초 1번 저장
    updated_at = models.DateTimeField(auto_now=True) #auto_now 데이터 수정될때마다 갱신

