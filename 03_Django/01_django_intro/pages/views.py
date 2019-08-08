from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.

#1. Baisc Logic( 기본 로직 )
def index(request):
    return render(request, 'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

def loremPicsum(request):
    return render(request, 'pages/loremPicsum.html')

#2. Template Variable( 템플릿 변수 )
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)

#3. Variable Routing( 동적 라우팅 )
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age,
        'pick': pick
    }
    return render(request, 'pages/hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용하여(name과 age를 인자로 받아) 자기소개 페이지
def my_introduce(request, name, age):
    location = ['철원', '안동', '울릉도', '인재']
    pick = random.choice(location)
    context = {
        'name': name,
        'age': age,
        'pick': pick
    }
    return render(request, 'pages/my_introduce.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def my_mul(request, num1, num2):

    context = {
        'num1': num1,
        'num2': num2,
        'num3': num1*num2
    }
    return render(request, 'pages/my_mul.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오.
def my_circle(request, r):
    context = {
        'r': r,
        'area': r**2*3.14,
    }
    return render(request, 'pages/my_circle.html', context)


#5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = ['보스몬스터']

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)

#6. 실습
#6-1. isbirth
def isbirth(request):
    today = datetime.now()

    if today.month == 4 and today.day == 7:
        result = True
    else:
        result = False
    context = {
        'result': result
    }

    return render(request, 'pages/isbirth.html', context)
    

#6-2. 회문판별(PALINDROME)
# 회문이면(반대로 돌려도 같은 글자 -EX,  racecar) '회문입니다.'
# 회문이 아니면 '회문이 아닙니다.'
def ispal(request, word):
    result = False
    if word == word[::-1]:
        result = True
    
    context = {
        'word': word,
        'result': result,
    }

    return render(request, 'pages/ispal.html', context)

#6-3. 로또 변호 추첨
# lottos -> 1~45 까지의 번호 중 6개를 랜덤으로 pick한 리스트
# real_lottos -> [21, 24, 30, 32, 40, 42]
#1. lottos 번호를 하나씩 출력(DTL-for문)
#2. 컴시기가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기(DTL-if문)
def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos = sorted(random.sample(range(1,45), 6))

    context = {
        'lottos': lottos,
        'real_lottos': real_lottos,
    }

    return render(request, 'pages/lotto.html', context)

#7. Form - GET ( 엔터를 치는 행위 : GET 요청, 주로 데이터를 조작하는 것이 아니라 읽기 위해 요청하는 것 )
def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)


def ping(request):
    return render(request, 'pages/ping.html')

def pong(request):
    ping = request.GET.get('ping')

    context = {
        'ping': ping
    }
    return render(request, 'pages/pong.html', context)

#8. Form - GET 실습( 아스키 아티 )
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')

    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)로 바꾼다.
    # 다음 받아온 str은 기준이 개행으로 되어있더라.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font(str)라는 변수에 저장
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시 요청을 보낸다. 그리고
    # 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {
        'result': result,
    }

    return render(request, 'pages/result.html', context)

#9. Form - POST ( 글을 쓰거나 수정하거나 삭제할때 사용 즉, 어떠한 처리를 해달라고 요청하는 것이다.
#  보안요소를 넣어놨다. 즉, 특정한 토큰을 넣어서 보내야한다. )
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }

    return render(request, 'pages/user_create.html', context)


#10. 정적 파일
def static_example(request):
    return render(request, 'pages/static_example.html')