from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.order_by('-id')

    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

# 글 생성
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect(f'/articles/{article.pk}/')

# 자세히 본다.
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 글 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/articles/')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect(f'/articles/{article.pk}/')