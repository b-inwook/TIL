# Web [HTML/DOM]

## 웹이란?

* 인터넷에 연결된, 컴퓨터를 통해, 사람들이 정보를 공유할 수 있는 전세계적 정보공간
* 웹을 구축에 서비스를 제공해 주는 것
* 우리는 브라우저를 통해서 서버에 요청을 보내고, 서버컴퓨터는 그에 맞는 응답을 준다,

* 요청의 종류

  1. 줘라 (Get) :   URL 뒤에 "?" 마크를 통해 URL의 끝을 알리면서, 데이터 표현의 시작점을 알린다.

  2. 받아라 (Post) : 처리할 내용을 보내면, 그에 맞는 처리를 하고 그 결과를 보내준다. POST 방식은 GET 방식과 달리, 데이터 전송을 기반으로 한 요청 메서드이다.

     GET방식은 URL에 데이터를 붙여서 보내는 반면, POST방식은 URL에 붙여서 보내지 않고

     BODY에다가 데이터를 넣어서 보낸다.  

앞으로 우리는 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.

---

##  Static Web

#### 정말 단순한 웹 서비스

남의 컴퓨터 주소 - 172.217.27.78 (주소 : 구글의 본래 주소)

http(s)://<u>google.com</u>

​                |-> 주소 : 

IP(Internet Protocol)

* 8비트 까지의 숫자로 구성된 숫자의 집합으로, 각자가 가지고 있는 주소와 동일하다.

도메인(Domain)

* 네트워크상의 컴퓨터를 식별하는 호스트명 위의 IP와 같이 주소를 의미한다.

URL(Uniform Resource Locator)

* 도메인 + 경로, 실제로 해당 서버에 저장된 자료의 위치



Static Web : 그 위치에 그 자료가 항상 있다.



Dynamic Web : 일반적인 웹사이트

Web Application program(web APP)



## WEB Page

W3C - 웹 표준

CSS, HTML, JS

HTML : Hyper Text Markup Language

* Hyper Text?

링크를 통해 순차적 텍스트 형태가 아닌 다중 연결성 텍스트

즉, Hyper Text를 주고받는 규칙 : Hyper TextTransfer Protocol - HTTP(S)

비연결 지향성. 서버가 응답을 주고 나면 연결을 끊는다.

* Markup

읽기 편하게 작성

* language

언어

HTML은  웹 페이지를 작성하기 위한 역할 표시 언어

CSS : Cascading Style Sheet

Java Script : 활기를 불어넣어줌



HTML 파일 : HTML 로 작성된 문서파일

DOCTYPE 선언부 : 사용하는 문서의 종류를 선언하는 부분. 보통 html을 사용한다

html 요소 : HTML 문서의 최상위 요소로 문서의 root를 뜻한다. head와 body 부분으로 구분된다.

head 요소 : 문서 제목, 문자코드(인코딩)와 같이 해당 문서 정보를 담고 있으며, 브라우저에 나타나지 않는다. CSS 선언 혹은 외부 로딩 파일 지정 등을 작성합니다. og와 같은 메타태그 선언이 이뤄진다.

body 요소 : 브라우저 화면에 나타나는 정보로 실제 내용에 해당한다.



## Tag와 DOM TREE(Document object model)

* 요소(Element)

<h1> contents</h1>

HTML의 elemetn는 태그와 내용으로 구성되어 있다.

태그는 대소문자를 구별하지 않으나, 소문자로 작성해야 한다.

물론, 요소간의 중첩도 가능하다.

* Self-closing element

닫는 태그가 없는 태그도 존재한다.

```html
<img src="url"/>
```

* 속성

태그에는 속성이 지정될 수 있다. 

링크를 걸어주는것

```html
<a href="google.com"/>
```

id: 유일한 식별자(중복 지정 불가능

class: 스타일시트에 정의된 class를 요소에 지정(중복 지정 가능)

style: 인라인 스타일을 지정

이 3가지는 태그와 상관없이 모두 사용 가능하다.

* DOM트리

태그는 중첩되어 사용가능하며, 이때다음과 같은 관계를 갖는다.

```html
<body>
    <h1>웹문서</h1>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
```

body태그와 h1태그는 부모(parent)-자식(child)관계

li태그는 형제 관계(sibling)

h1태그와ul 태그는 형제 관계(sibling)

* 시맨틱태그

컨텐츠의 의미를 설명하는 태그로서, HTML5에 새롭게 추가된 시맨틱 태그가 있다.

하지만, 공간 자체에 대한 어떠한 의미도 가지고 있지 않다.

```html
<div>이거슨 공간</div>    <!--division, 공간 분할--!>
```

개발자가 의도한 요소의 의마가 명확히 보이며, 코드의 가독성을 높이고 유지보수가 쉽다는 장점!

+++ 웹에 존재하는 수많은 웹페이지들에 '메타데이터'를 부여하여 기존의 잡다한 데이터의 집합을 '의미'와 '관련성'을 가지는 거대한 데이터의 집합으로 구축하고자 하는 발상!

개발자 및 사용자 뿐만 아니라 검색엔진(구글, 네이버) 등에 의미 있는 정보의 그룹을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 의미를 가지는 태그들을 활용하기 위한 노력

** non semantic 요소 -> div, span 등 -> 그저 공간을 만들어주는 태그

* SEO(Search Engine Optimization)

웹 페이지 검색 엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성해서 검색 결과의 상위에 노출될 수 있도록 하는 작업이다. 그래서 시맨틱 태그가 중요하고 투자를 많이하고 있다.

* 의미를 부여함

---

header : 헤더(문서 전체나 섹션의 헤더)

nav : 네비게이션

aside : 사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용

section : 문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 h1~h6 요소를 가짐

article : 문서, 페이지, 사이트안셍서 독립적으로 구분되는 영역(포럼/신문 등의 글 또는 기사)

footer : 푸터(문서 전체나 섹션의 푸터)

---



## Markup - Tag 의 종류 (어떤 역할 / 어떤 태그)

* 텍스트 태그

```html 
<h1>contents</h1> : 제목
<p1>contents</p1> : 본문
<b>contents</b> : 글자 강조(non semantic)
<strong>contents</strong> : 글자 강조(semantic) 정말 중요한 내용 강조
<ol> 
    <li>순서있는</li>
    <li>항목</li>
</ol>: Ordered List 의 약자로 순서가 있는 목록. 번호 형식으로 순서를 매겨 목록을 만드는 형식이다.
<ul> : unoerdered List 글머리 기호를 붙혀서 목록을 만듬.
   <li>순서있는</li>
    <li>항목</li> 
</ul>
```

* 레이아웃 태그 - non-semantic 태그

```html
<div>의미없는 블록</div>
<span>의미 없는 인라인</span>
```

* 링크 태그

```html
<a href="google.com"/>
```

속성값을 정해주면 따라가는 링크

* 미디어 태그

```html
<img src="/profile.jpg"/>
```

1. tabindex: 사용자가 탭을 누를 때의 순서 지정
2. alt: 이미지가 로드되지 않을 때 보여지는 문구
3. width: 이미지 너비 지정
4. height: 이미지 높이 지정

* video 태그에 사용되는 추가 속성
  1. 오토 플레이: 동영상

* Iframe 태그에 사용되는 추가 속성
  1. width: 아이프레임 창의 가로 길이 결정
  2. height: 아이프레임 창의 세로 길이 결정