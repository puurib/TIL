from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    content = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', content)

# new, create가 create하는 함수들
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

def create(request):
    if request.method== 'POST':
        form = ArticleForm(request.POST) #request.POST를 적으면 바인딩된 폼 아래 주석과 같음
        if form.is_valid():  # 모델을 참조한 유효성검사 (비어있는지 안비어있는지 기술된 조건에 맞는지)
            article = form.save() # 이미 저장이 되고, article에 대입됨
            # form.save()는 리턴값이 생성된 객체가 있음.
            # 그 객체를 article로 담아줌
            return redirect('articles:detail', article.pk)
    
    else: #  GET방식
        form = ArticleForm() # 빈 form 생성
    # 유효성검사에서 예를들어 10자리를 넘거나, GET방식 등이라면
    context = {
    'form': form,
    }
    return render(request, 'articles/create.html', context) # 자동으로 else처리

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article= Article(
    #     title=title,
    #     content=content
    # )
        


def detail(request, pk): # url에서 넘겨주는 값 pk도 인자로 받아줌
    article = Article.objects.get(pk=pk)
    content = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', content)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    content = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', content)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method== 'POST':
        form = ArticleForm(request.POST, instance=article) #request.POST를 적으면 바인딩된 폼 아래 주석과 같음
        if form.is_valid():  # 모델을 참조한 유효성검사 (비어있는지 안비어있는지 기술된 조건에 맞는지)
            article = form.save() # 이미 저장이 되고, article에 대입됨
            return redirect('articles:detail', article.pk)
    
    else: #  GET방식 /  instance=article 가 있어서 수정(not새로 생성)
        form = ArticleForm(instance=article) 
    context = {
    'form': form,
    'article' : article,
    }
    return render(request, 'articles/update.html', context)
    # article = Article.objects.get(pk=pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # # 수정했으니 상세 페이지로 이동
    # return redirect('articles:detail', pk)