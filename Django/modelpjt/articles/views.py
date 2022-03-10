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

    # article.id = article.pk
    # return redirect('articles:detail', article.id)
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article} 
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    #1. pk에 해당하는 글을 db에서 가져온다
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        #2. 해당글을 삭제합니다.
        article.delete()
        #3. index페이지로 이동합니다
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
    

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context= {'article':article}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 수정할 article을 가져온다.
    article = Article.objects.get(pk=pk)

    # 2. request로 부터 사용자가 입력한 데이터를 가져온다
    # edit.html의 input의 name따라서 
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. article을 수정한다
    article.save()
    # 4. article 상세페이지로 보낸다.
    return redirect('articles:detail', article.pk)