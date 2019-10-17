from django.urls import path
from . import views 

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # GET
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), # GET(new), POST(crete)
    path('<int:article_pk>/', views.detail, name='detail'), # GET
    path('<int:article_pk>/delete/', views.delete, name='delete'), # POST
    # 무언가 삭제하므로 delete 명시
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'), # GET(edit), POST(update)
    # pk를 int로 변수화시켜, views.detail의 매개변수 pk로 들어간다.
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/update/', views.comments_update, name='comments_update'),
    # path의 요소는 단순한 명시. 이름은 달라도 된다. 단, comment_pk에 해당하는 자료명은 views에 만든 함수와 동일해야한다.
]