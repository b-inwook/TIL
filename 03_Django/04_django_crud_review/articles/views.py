from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article, Comment
from IPython import embed

def index(request):
    # articles = Article.objects.all()[::-1]
    # article의 모든 것을 불러와 articles에 저장
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def create(request):
    # POST 요청일 때
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.save()
        # embed()
        return redirect('articles:detail', article.pk)
    # GET 요청일 때
    else:
        return render(request, 'articles/create.html')
    """
    title = request.POST.get('title')
    # print(title)
    content = request.POST.get('content')

    #1. 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2. 두번째 방법
    article = Article(title=title, content=content)
    article.save()

    #3. 세번째 방법
    # Article.objects.create(title=title, content=content)

    return redirect(f'/articles/{article.pk}/')
    # redirect는 경로 설정, render는 파일을 보여주는 것
    # 따라서, redirect는 네이밍한 경로 사용가능
    # 랜더하여 새로운 화면을 띄우는게 아니라 다시 한번 돌아가는것.
    # render 는 템플릿을 불러오고, redirect 는 URL로 이동합니다.
    # URL 로 이동한다는 건 그 URL 에 맞는 views 가 다시 실행될테고
    # 여기서 render 를 할지 다시 redirect 할지 결정할 것 입니다. 

    # GET 요청 : 정보(HTML file)를 조회, 신원확인이 필요가 없음, 
    # 스키마 정보가 노출, 캐싱할 수 있다.
    # POST 요청 : URL에 데이터를 노축하지 않고 요청,
    # 기본보안이 되어있다. 캐싱할 수 없다.
    """
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # comments = Comment.objects.all()
    # 모든 댓글을 다 가져와줘
    comments = article.comments.all()
    context = {'article': article, 'comments': comments, }
    # embed()
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def update(request, article_pk):
    # embed()
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)

def comments_update(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('articles:detail', article_pk)
    else:
        context = {'comment': comment}
        return render(request, 'articles/comment_update.html', context)