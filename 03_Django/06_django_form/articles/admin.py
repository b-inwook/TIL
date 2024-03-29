from django.contrib import admin
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

# admin.stie.register(Article, ArticleAdmin) # 이렇게도 할 수 있다.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at',)

#admin.site.register(Comment, CommentAdmin)