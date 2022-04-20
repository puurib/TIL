from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('articles',)
        #fields = ('id', 'title',)
        
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        #fields = '__all__'
        fields = ('id', 'title',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    # Article 1개에 Comments 여러개 
    # read_only 하나만 줄때는 
    #comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    comment_set = CommentSerializer(many=True, read_only = True)
    
    class Meta:
        model = Article
        fields = '__all__'
        #fields = ('id', 'title',)

