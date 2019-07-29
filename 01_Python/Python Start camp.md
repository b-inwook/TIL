# 2019.07.15. StartCamp Review

open source를 가지고 써라.

API 서로 다른 서비스가 통신하기 위해 사용 ex) 배달의민족 로그인 시 페이스북 아이디 요청/반환

CLI : 서로다른 웹에 통신을 하기 위함

Web Crawling : 사람에게 보여주기 위해 끌어오는것

git & GitHub : git이라는  GitHub이라는 원격저장장소에 저장하는 것

GitHub Page



# 2019.07.15. 앞으로

HTML & CSS

Flask( variable routing, html render ...) 마이크로 웹 프레임 워크

SQL

Client & Server ( 장고 ) 요청/반응

Telegram 

HEROKU 배포

aws 배포

Responsive Web : 동적으로 계속 바꿔주는 것

JS

Vue.js

# 2019.07.15. PYTHON

jupyer tool을 사용할 것이다. 머신러닝

python -m notebook

Y : 코드 수정 / m : 마크다운

현재 셀을 수정 : enter

현재 셀을 실행 : ctrl + enter

셀 위에 추가 : a

셀 아래 추가 : b

셀 제거 : dd

help : h

---

x, y = 1, 2 에서 뿌려주는 것 unpack이라고 한다.



## 수치형(numbers)

docstring

import sys 에 관해서 정리하기

arbitrary-precision arithmetic을 사용; 유동적으로 메모리를 관리하기 때문에 다음이 가능

```python
import sys

max_int = sys.maxsize
print(max_int)
a = sys.maxsize * sys.maxsize
print(a)
```

---

round()

```python
round(3.5 - 3.12, 2)
```

output은 다음과 같다.

```
0.38
```

기본적으로 파이썬은

3.5 - 3.12 == 0.38 시 False 이기 때문에 round()함수를 적절히 사용할 것.

---

아래 3개는 같은 표현

```python
a = 3.5 - 3.12
b = 0.38

abs(a - b) <= 1e-10
```

```python
import sys

abs(a - b) <= sys.float_info.epsilon
```

```python
import math
math.isclose(a, b)
```

---

복소수

```python
a = 3 - 4j
print(a.imag)  # 허수부
print(a.real)  # 실수부
print(a.conjugate())  # 켤레복소수
```

출력

```python
-4.0
3.0
(3+4j)
```

---

print('내용을 띄워서 출력하고 싶으면?', end='\t')

여기서 end='\n'  이 기본이다. 그래서 print()함수가 개행이 포함되는 것

---

python에서는 -5 ~ 256까지 id는 동일하다.

그 외의 값은 다른 주소값을 가짐;

그래서

```python
a = 257
b = 257
a is b
```

```
False
```

---

문자열은 인덱싱을 통해 값에 접근할 수 있다.

print('Hi'[1])

---

[리스트]

```
l = []
ll = list()
```

[튜플]

```python
a = (1)
print(type(a))
b = (1,)
print(type(b))
```

```python
<class 'int'>
<class 'tuple'>
```



