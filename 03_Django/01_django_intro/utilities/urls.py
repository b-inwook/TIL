from django.urls import path
from . import views

# 여기서 인덱스 page는 보통 빈 string ('')으로 표현한다.
urlpatterns = [
    path('', views.index),
    path('papagu/', views.papagu),
    path('translated/',views.translated),
]