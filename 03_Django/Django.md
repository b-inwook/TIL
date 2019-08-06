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

source venv/Scripts/activate - 가상환경 activate

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

반환에 3번째 항은 딕셔너리다.

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

