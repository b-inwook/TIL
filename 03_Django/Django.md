# Django

web service에서 sever의 입장

MTV

Model : 데이터를 관리

Template : 사용자가 보는 화면

View : 중간 관리자

사용자 -> 요청 -> View -> Model이 Database에서 찾고 View에게 줌-> View가 Template을 통해 사용자에게 보여줌(Html)

---

python -m venv venv - 가상환경 만든다.

pip list - 이때 이 명령어를 보면 전역 라이브러리가 모두 보임

---

code . 으로 열자

source venv/Scripts/activate - 가상환경 활성화

pip list - 깨끗한 환경임을 확인 할 수 있다.

pip install django - 장고설치

pip list - 장고가 설치 된것을 확인할 수 있다.

django-admin startproject django_intro .  - 프로젝트만든다 ( . )을 찍어야지 현재 디렉토리에서 프로젝트가 시작

python manage.py startapp [이름] : 앱의 기본 내용물 생성

INSTALLED_APPS에 앱이름 추가// 이때, ( , )꼭 적어주기.

 ++ 추가정보 ) python manage.py runserver - 서버 실행

---

앱을 등록하면 프로젝트에 기술해야 함 => settings.py => INSTALLED_APPS

```django
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

마지막에 콤마를 꼭 찍어야 한다.

한국어, 시간설정도 바꿀수 있다.

```django
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

---

```django
from home import views

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```

url을 views안에 index함수로 보낼 것이다.

우선 import를 시키고

views에 index함수를 만들자

```django
from django.shortcuts import render

# Create your views here.

#1. Baisc Logic( 기본 로직 )
def index(request):
    return render(request, 'index.html')
```

---

APP안에 templates 폴더를 만들고, html 파일을 만든다.

---

```django
#2. Template Variable( 템플릿 변수 )
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    return render(Request, 'dinner.html', {'pcik':pcik})
```

반환 render에 3번째 항은 딕셔너리다.

---

```django
#3. Variable Routing( 동적 라우팅 )
def hello(request, name):
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    # name = random.choice(names)
    context = {'name':name}
    return render(request, 'hello.html', context)
```

```django
path('hello/<name>/',views.hello),
<>안은 디폴트값이 str이다.
```

---

### 두개의 APP을 만드는 경우

```django
# 프로젝트의 urls.py에서 설정
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('utilities/', include('utilities.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
```

```
# pages, utilities에 별도의 urls.py 파일을 만든다.
from django.urls import path
from . import views 
# 여기서 .은 형제 디렉토리 즉, 같은 디렉토리 내에 있는 파일에 접근한다는 뜻.

urlpatterns = [
    path('art/', views.art)
]
```

---

이때, INSTALLED_APPS에 등록된 순서대로 templates의 html이 있는지 찾는다.

장고에서는 이 문제를 templates에 APP파일을 만들어 해결한다.

```
# pages -> templates -> pages : 동일한 앱이름으로 폴더를 만든다.
# 그안에 html 파일을 넣는다.

# 그리고 views파일을 다음과 같이 수정해야한다.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
```



---

### 상속의 개념

프로젝트 폴더 밑에 templates 폴더를 만든다.

그 안에 base.html을 만든다.

장고가 이 templates를 알기위해서 별도로 알려줘야한다.

```
#settings.py 에서 DIRS를 다음과 같이 수정한다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_intro','templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```
#이제 base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <h1 class="text-center">Template Inheritance</h1>
    <hr>
    <!--포털이 열린 것-->
    {% block body %}
    {% endblock %}

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>

## html 파일들에게 템플릿 상속을 주기 위해 다음과 같이 준다.
{% extends 'base.html' %}

{% block body %}
    <h1>원의 넓이</h1>
    <p>반지름이 {{ r }}인 원의 넓이는 {{ area }}입니다.</p>
{% endblock %}
```

---



# Database SQL 기초

데이터베이스(DB) : 체계화된 데이터의 모임

몇개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없앰



RDBMS(관계형데이터베이스 관리 시스템)

관계형 모델을 기반으로하는 데이터베이스 ....

SQLite : 장고에 기본 내장 데이터베이스로 사용

---

* 스키마: 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조

열 - 필드 / 행 - 레코드 

PK(기본키) : 각 행(레코드)의 고유값으로 Primary Key로 불린다. 반드시 설정해야하며, 데이터베이스 관리 및 관계 설명서 주요하게 활용된다.

---

SQL(Structured Query Language)는 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그램.

테이블에 데이터 삽입 (새로운 행 추가) -> INSERT

데이터 삭제 (행 제거) -> DELETE

---

database <--SQL--> Code

---

Object Relational Mapping

-> ORM

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 (Djngo - SQL) 데이터를 변환하는 프로그램

---

Database <----ORM----> Python Code

---

SQL 문법을 몰라도 쿼리(데이터베이스에 정보를 요청) 조작 가능

객체 지향적인 접근 가능 (인스턴스 / 클래스 변수 etc.)

해당 객체의 재홀용 가능

...

즉, python의 class로 DB를 조작 가능.

---

### DB를 다루어 보자

python manage.py makemigrations :  설계도를 만드는 것

```django
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10) # max_length 설정 필요
    content = models.TextField() # 글자의 제한이 없다.
    created_at = models.DateTimeField(auto_now_add=True) # 마찬가지로 필요하다.
    updated_at = models.DateTimeField(auto_now=True)  # 계속 들어갈때마다 시간을 수정해줌
```

migrations는 확인용임. 들어가서 확인해봐라.

---

python manage.py migrate : 실제 데이터베이스에 적용. 그러면 db.sqlite3가 뜬다.

---

### DB를 조작해보자

python manage.py shell : 파이썬 shell을 다룰 수있음

파이썬 클래스로 DB를 조작하는데 object가 도와준다. 마치 번역기처럼

```
from articles.models import Article
Article.objects.all()
article = Article() # 객체 생성
article.title = 'first' # 클래스 변수로 접근 #1번째 저장방법

article.save() # DB에 저장하기위해 메서드 호출 <<< 필수!!!>>>

article # object(1)이라고 뜬다. 저장된 것을 확인 하려면 다음과 같이...
article.title
article.created_at # 장고가 알아서 넣어주는 것

article = Article(title='second', content='django!') #이렇게도 저장할 수 있다.#2번째
article.save()

Article.objects.get(pk=1): pk=1인값만 가져온다.

articles = Article.objects.all() # 변수에 저장하여 확인도 가능하고.
articles
article.objects.all() # 바로 모두 확인가능

Article.objects.create(title='third', content='django!') # save()없이 바로 저장되는 방법 #3번째 , 또한 바로 str이 출력됨
```

```
article.id 는 저장되었을 때만 값이 나온다.
article.full_clean : 지우는 것
article = Article.objects.filter(title='first') ; 타이틀이 first인 것만 저장한다
article = Article.objects.filter(title='first').first() : 메서드 체이닝이 가능
# 첫번째꺼가 저장됨.
# first(), last() 두개만 된다. 다른것들은 안됨

article = Article.objects.get(pk=1) : pk=1인값만 가져온다. 고유한 값이다. 중복되면 오류
그래서 다음과 같으면 오류가 발생한다.(아래는 first라는 타이틀이 많은 경우임.)
그래서 .get은 pk로만 쓴다. 마찬가지로 없는 pk를 접근 할 수 없다. 에러발생.

article = Article.objects.get(title='first')
없거나 중복되는 항목에 대해서
.get()은 에러. // 타입은 Article 객체 ; 그래서 article.id , article.content이가 가능하다.
.filter()는 에러 안난다. => 빈 Queryset을 반환함. // 타입은 쿼리셋 ; 그래서 슬라이싱 가능

article = Article.objects.order_by('id') : id를 기준으로 오름차순 정렬
article = Article.objects.order_by('-id') : id를 기준으로 내림차순 정렬
article = Article.objects.all()[2] : 해당원소에 해당하는 객체

Update:
article.title = 'byebye'
article.save()
article
article : 1번글 - byebye : django! 로 바뀜
Delete:
article.delete()
별도 save 없음 -> delete 는 이미 끝난 파일
```

---

admin.site.register(Article) : Article 추가하기

```
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
# 이쁘게 엑셀형태로 변함
admin.site.register(Article, ArticleAdmin)
```

```
pip install django-extension  (-는 설치)
crud -> installed apps -> django_extensions 기입  (_는 등록)
이걸 사용하면 우리는 import를 별도로 해주지 않아도 된다. 매우 편안
```



### CRUD 다뤄보자

basic settings!!!

```
python -m venv venv
source venv/Scripts/activate
django-admin startproject crud .
python manage.py startapp articles
출생신고 : crud -> settings.py -> INSTALLED_APPS
```

```
# 프로젝트안에 urls.py 작성
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls'))
    path('admin/', admin.site.urls),
]
```

```
# 앱안에 urls.py 작성;
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]
```

```
# basic.html 작성
```

```
# 모델
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'
```

```
python manage.py makemigrations
python manage.py migrate
```

```
# views.py
from django.shortcuts import render, redirect
from .models import Article

def index(request):
    #articles = Article.object.all()[::-1]
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('/articles')
```

```
# index.html
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">Articles</h1>
    <hr>
    {% for article in articles %}
        <p>글 번호: {{ article.id }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
        <hr>
    {% endfor %}
    <a href="/articles/new/">[글쓰기]</a>
{% endblock %}
```

```
# new.html
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">NEW PAGE</h1>
    <form action="/articles/create/" method="POST">
        {% csrf_token %}
        <label for="title">Title</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="content">Content</label><br>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="글쓰기">
    </form>
    <a href="/articles/" target="_blank">[메인 페이지로 돌아가기]</a>
{% endblock %}
여기서 _blank는 새창에서 띄우기
```

```
# create.html
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">글이 성공적으로 작성되었습니다.</h1>
{% endblock %}
```

```\
# update => views.py
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
```

```
# edit.html
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">EDIT</h1>
    <form action="/articles/{{ article.pk }}/update/" method="POST">
        {% csrf_token %}
        <label for="title">Title</label><br>
        <input type="text" id="title" name="title" value="{{ article.title }}"><br>
        <label for="content">Content</label><br>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
        <input type="submit" value="수정완료">
    </form>
    <a href="/articles/" target="_self"></a>
{% endblock %}
```

```
# 디테일에 버튼을 넣어주자
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">DETAIL</h1>
    <h2>{{ article.pk }}번글</h2> <!-- id나 pk나 똑같이 사용가능 -->
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <p>글 작성시간: {{ article.created_at }}</p>
    <p>글 생성시간: {{ article.updated_at }}</p>
    <hr>
    <a href="/articles/{{ article.pk }}/edit/" target="_self">[글 수정]</a><br>
    <a href="/articles/{{ article.pk }}/delete/">[글 삭제]</a><br>
    <a href="/articles/">[메인 페이지로 가기]</a>
{% endblock %}
```

