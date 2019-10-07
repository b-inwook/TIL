from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article
from IPython import embed

def index(request):
    # articles = Article.objects.all()[::-1] # article의 모든 것을 불러와 articles에 저장

    articles = Article.objects.order_by('-pk')
    context = {'articles': articles} # dictionary
    return render(request, 'articles/index.html', context)

def create(request):
    # POST 요청일 때
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    # GET 요청일 때
    else:
        return render(request, 'articles/create.html')


    # try:
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article = Article(title=title, content=content)
    #     article.full_clean()
    # except ValidationError:
    #     raise ValidationError('Your Error Message')
    # else:
    #     article.save()
    #     return redirect('articles:detail', article.pk)
    # redirect는 경로 설정, render는 파일을 보여주는 것
    # 따라서, redirect는 네이밍한 경로 사용가능


    #
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    #
    # 저장하는 방법
    #1. 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2. 두번째 방법
    # article = Article(title=title, content=content)
    # article.save()

    #3. 세번재 방법
    # Article.objects.create(title=title, content=content)

    # return redirect(f'/articles/{article.pk}/')
    # 랜더하여 새로운 화면을 띄우는게 아니라 다시 한번 돌아가는것.
    # render 는 템플릿을 불러오고, redirect 는 URL로 이동합니다.
    # URL 로 이동한다는 건 그 URL 에 맞는 views 가 다시 실행될테고 여기서 render 를 할지 다시 redirect 할지 결정할 것 입니다. 

    # GET 요청 : 정보(HTML file)를 조회, 신원확인이 필요가 없음, 스키마 정보가 노출, 캐싱할 수 있다.
    # POST 요청 : URL에 데이터를 노축하지 않고 요청, 기본보안이 되어있다. 캐싱할 수 없다.

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        # else문을 사용하면 원하는 곳으로 보낼 수도 있다.
        return redirect('articles:detail', article.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article' : article}
        return render(request, 'articles/update.html', context)