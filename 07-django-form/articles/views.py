from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    # 요청의 메서드가 POST라면, create 로직을 수행
    if request.method == 'POST':
        form = ArticleForm(request.POST) # request.POST에 담긴 데이터로 ArticleForm을 생성
        # 유효성 검사
        if form.is_valid(): # 함수나 메서드가 is_로 시작하는거면, 해당 함수나 메서드의 결과는 True/False
            article = form.save()
            return redirect('articles:detail', article.pk) # is_valid 통과 못했을 때
            # return redirect('articles:index')
    
    # 요청의 메서드가 POST가 아니라면, new 로직을 수행 & create와 동일한 로직을 수정해줌 (중복 없애기!)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    #return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청의 method가 POST라면, update
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
        
    
    # POST가 아니라면, edit 페이지 표출
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

