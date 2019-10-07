from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),  # GET 
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), # GET(new), POST(create)
    path('<int:pk>/', views.detail, name='detail'),  # GET
    path('<int:pk>/delete/', views.delete, name='delete'), # POST
    # 무언가 삭제하므로 delete 명시
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'), # GET(edit), POST(update)
    # pk를 int로 변수화시켜, views.detail의 매개변수 pk로 들어간다.
]