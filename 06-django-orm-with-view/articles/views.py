from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all() # -> QuerySet 형태
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk) # 조회한 결과가 2개 이상이거나 없으면 에러가 남.
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # CREATE 방법
    # 1. 
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. -> 이 방법 사용함
    article = Article(title=title, content=content)
    article.save()

    # 3.
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')

def delete(request, pk):
    # 몇 번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글을 삭제
    article.delete()
    return

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)


