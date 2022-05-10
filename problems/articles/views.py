from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
def article_list(request):
    # Q 1.
    # Q 2.
    pass


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # Q 3.
    # Q 4.
    # Q 5.
    pass


@api_view(['GET'])
def comment_list(request):
    # Q 7.
    pass

@api_view(['POST'])
def comment_create(request, article_pk):
    # Q 8.
    pass

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
    # Q 10.
    pass

