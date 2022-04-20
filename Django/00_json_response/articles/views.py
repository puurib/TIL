from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

from .models import Article, Comment
from .serializers import (
    ArticleSerializer, 
    ArticleDetailSerializer,
    CommentSerializer
)
from .models import Article


@api_view(['GET', 'POST'])
#@api_view()
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #print(">>>>>>", request.data)
        serializer = ArticleDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"result":"success"}, status=status.HTTP_201_CREATED)
        
        # raise_exception 넣어줘서 주석처리
        # return Response({"result":"fail"}, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response({"result":"deleted"}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

@api_view(['POST', 'GET'])
def article_comment_list(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

        
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def comment_detail(request, comment_pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)



# Create your views here.
# def article_html(request):
#     articles = Article.objects.all()
#     context = {
#         'articles': articles,
#     }
#     return render(request, 'articles/article.html', context)


# def article_json_1(request):
#     articles = Article.objects.all()
#     articles_json = []

#     for article in articles:
#         articles_json.append(
#             {
#                 'id': article.pk,
#                 'title': article.title,
#                 'content': article.content,
#                 'created_at': article.created_at,
#                 'updated_at': article.updated_at,
#             }
#         )
#     return JsonResponse(articles_json, safe=False)


# def article_json_2(request):
#     articles = Article.objects.all()
#     data = serializers.serialize('json', articles)
#     return HttpResponse(data, content_type='application/json')


