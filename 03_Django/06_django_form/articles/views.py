from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles,} # dictionary
    return render(request, 'articles/index.html', context)

def create(request):
    """
    Form Class
    모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 데이터 정제 후 DB에 실제 저장하는 로직 필요

    Model Form
    이미 Model에 대한 정보(스키마)를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고 있음.
    form.save()만 해도 DB에 저장 됨
    """


    # POST 요청일 때
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
            # embed()
            # model form의 경우 위 한 줄로 처리할 수 있다.
            # model에 대한 정보가 form.py에 선언해줬기 때문에, db에 저장가능하다.
            # 즉, model form을 사용하면 불필요한 작업을 생략가능하다.
            

            
            # form.cleaned_data를 통해 폼 데이터를 정제한다.(form.cleaned_data -> Dict)
            """
            
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            """

            # embed()
            # .create(.save() 필요없다!! - 3번쨰 방법)
            # article.save()

    # GET 요청일 때
    else:
        form = ArticleForm()
        # embed()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    # 500은 서버 잘못이다.
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
        }
    return render(request, 'articles/detail.html', context)

# POST요청 밖에 못받는다. POST요청이 아니라면 redirect
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index') # redirect -> GET 요청

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # instance-> 수정의 대상이 되는 특정한 글 객체
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # embed()
            return redirect('articles:detail', article.pk)

            '''
            article.title = form.cleaned_data.get('title') # cleaned_data로 form을 유효성 검사를 하면, 딕셔너리로 출력되고, 이를 get함수를 사용 할 수있다.
            article.content = form.cleaned_data.get('content')
            article.save()
            '''

    else:
        """
        # 기존에 사용했던 글
        # 방법1.

        # form = ArticleForm(initial={
        #     'title': article.title,
        #     'content': article.content,
        # })

        # 방법2.

        # form = ArticleForm(initial=article.__dict__)
        # embed()
        """

        form = ArticleForm(instance=article)
        # embed()
    context = {'form': form, 'article': article}
    return render(request, 'articles/form.html', context)




"""
* CREATE & UPDATE는 html 파일 공유 
Create 로직
1. GET
- 사용자가 데이터를 입력 할 수 있는 빈 Form을 제공
2. POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1. GET
- 기존 사용자의 글이 입력된 (이미 채워진) Form 제공
2. POST
- 수정된 글을 DB에 저장
"""

@require_POST
def comments_create(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid(): # 유효성 검사
        comment = comment_form.save(commit=False) # comment_form의 정보를 DB에 저장하지않고, comment에 저장한다.
        comment.article_id = article_pk # comment에 article 정보를 넣어야한다.
        comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
