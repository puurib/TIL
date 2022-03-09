from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    obj = Article.objects.order_by('-pk')
    #obj = Article.objects.all()[::-1]
    # 쿼리셋은 슬라이싱이 가능하다. 최신순으로 정렬
    print(obj)
    context= {
        'obj': obj
    }
    return render(request, 'articles/index.html', context)

def new(request):

    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content=request.POST.get('content')
    #print(f'title : {title}, content: {content}')
    #DB에 데이터 저장하기
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')