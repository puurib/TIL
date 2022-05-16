### [8] serializers.py

- `accounts > serializers.py`

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content',)
            
    articles = ArticleSerializer(many=True)
    #like_articles = ArticleSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'articles',)
```

- `community> serializers.py`

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment, Vote

User = get_user_model()

# 댓글
class CommentSerializer(serializers.ModelSerializer):   
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article',)
        read_only_fields = ('article', )


# 
class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comments', 'like_user')


# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'comment_count', 'like_count')


class VoteSerializer(serializers.ModelSerializer):
    pass
```

- `movies > serializers.py`

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genre',)

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields  = ('id', 'title', 'release_date', 'running_time', 'poster_path', 'genres',)
        read_only_fields  = ('article')
        #fields = '__all__'
```

### [9] views.py

- `accounts > views.py`

```python
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```