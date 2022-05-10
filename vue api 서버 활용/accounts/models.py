from django.db import models

'''
아래는 작성한 코드
'''
from django.contrib.auth.models import AbstractUser # 확장만 시키고 상속시켜줌

class User(AbstractUser):
    pass