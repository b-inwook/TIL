from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Movies, Comments
from .form import MoviesForm, CommentsForm

def index(requeset):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        movies_form = MoviesForm(request.POST)
        if movies_form.is_vaild():
            movie = movies_form.save()
            return redirect('movies:detail', movie_id)
    else:
        movies_form = MoviesForm(request.POST)
        context = {
            'movies_form':movies_form,
        }
    return render(request, 'movies/create.html', context)

def detail(request):
    movie = get_object_or_404(Movies, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comment_form':comment_form,
        'comments':comments,
        }
    return render(request, 'articles/detail.html', context)

def update(reqeust):
    if request.method == 'POST':
        movies_form = MoviesForm(request.POST, instance=article)
        if movies_form.is_valid():
            movies_form.save()
            return redirect('articles:detail', article.pk)
    else:
        movies_form = ArticleForm(instance=article)
    context = {'movies_form': movies_form, 'article': article}
    return render(request, 'articles/form.html', context)

@require_POST
def comments_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # comment_form의 정보를 DB에 저장하지않고, comment에 저장한다.
        comment.article_id = article_pk # comment에 article 정보를 넣어야한다.
        comment.save()
    return redirect('articles:detail', article_pk)