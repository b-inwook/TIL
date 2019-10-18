from django import forms
from .models import Moives, Comments

class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        field = ('title', 'title_en', 'audience', 'open_date', 'genre', 'watch_grade', 'score', 'poster_url', 'descriptions',)


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        field = ('content', 'score',)