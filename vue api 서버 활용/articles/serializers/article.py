'''
model serializers 사용할 예정
'''

from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article # model serializers에서는 model을 지정해줘야함
        pass