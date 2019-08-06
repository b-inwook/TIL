# CSS (Cascading Style Sheet)

* 이쁘게 꾸며주는도구 / 스타일링

```css
hi{color;font-size:15px;}
셀렉터(h1) / 프로퍼티(color) / 값(blue)
```



* 기본 사용법(주석)

```css
/*주석은 이 사이에 적어주세요.*/
```

* CSS 활용하기 1. Inline(인라인)

html 요소의 style에 CSS를 넣기 (좋은 방법이 아니다.)

* CSS 활용하기 2. Embedding(내부참조)

html 내부에 CSS 포함시키기 (h1 내부에 color 선언 후 작동)

* CSS 활용하기 3. link file(외부참조)

외부에 있는 CSS파일 불러오기

---

* 실제로 project에 사용해야 하는 것은?

'컴포넌트화'

일반적으로 외부 파일로서 활용한다!

css 파일별로 만들어서 필요할 때 가지고 와서 사용한다.



### 단순 선택자(기본)

* 기본선택자

{color; blue}

ol, ul {list}

a



* 클래스 선택자

.class {color: blue;}

  		프로퍼티  값

​          (property)(value)



*  후손/자식 셀럭터

자식 셀렉터(공백) -> 해당 태그 내에 있는 직계 자식 요소만 선택

후손 셀렉터(>) -> 해당 태그 내의 모든 요소를 선택



### CSS 프로퍼티 값의 단위

1. 키워드 2. 크기단위 3. 색깔
2. 1 픽셀이란?

: 많은 픽셀(화소)는 3X3 픽셀 보다 16ㅌ

2. 2 ~~~

2. 3 em : 부모의 (픽셀단위)를 배수로 환산 ex) 부모 50px => 자신 1em = 50px

2. 4 rem : em의 기준은 상속의 영향으로 바뀔 수 있다. 즉, 상황에 따라 1.2em은 각기 다른 값을 가질 수 있다. rem은 최상위 요소(html)의 사이즈를 기준으로 삼는다. rem의 r은 root를 의미한다.

2. 5 viewprot 단위 : 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 상대적인 단위인 viewport를 기준으로 만든 단위
3. 색상 표현 단위- Hex

```css
#div1 {
    color: #ff0000;   /* 빨강색 */
}
#div2 {
    color: rgb(255, 0, 0);  /* 빨강색 */
}
#div3 {
    color: rgb(255, 0, 0, 0.2);  /*마지막 항은 투명도 설정*/
}
```

* box 모델 구성

Border : 테두리 영역

Margin : 테두리 바깥의 외부 여백 배경색을 지정할 수 없다.

Padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경의 컬러, 이미지는 패딩까지 적용

contents : 실제 내용이 위치

* 기본 박스모델 활용
  1. margin
  2. padding
  3. border
  4. shorthand



* display 속성(box 들이 어떻게 보여지는지)

  * block : 항상 새로운 라인에서 시작한다. 화면 크기 전체의 가로폭을 차지한다. (width: 100%) 너비가 정해지면 나머지를 margin으로

  * inline : 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다. content의 너비만큼 가로폭을 차지한다. width, height, margin-top, margin-bottom 프로퍼티를 지정할 수 없다. 상, 하 여백은 line-height로 설정한다.

  * inline-block : 블락과 인라인 레벨 요소의 특징을 모두 갖음 인라인 레벨 처럼 한 줄에 표시됨 블락에서의 위드 하이츠 마진(탑, 바텀) 속성을 모두 지정할 수 있다.

  * None : 해당 요소를 화면에 표시 X / 공간(영역) 조차 사라짐

    visibility, hidden, none



1. static(기본위치)
2. relative(상대위치) : 기본 위치 (static) 를 기준으로 좌표 프로퍼티(top, bottom, left, right)를 사용하여 위치를 이동( 음수도 가능)
3. absolute(절대위치): 부모를 기준으로..
4. fixed(고정위치) : 부모 요소와 관계없이.. 



* <element>:nth-child(n) VS <element>:nth-of-type(n)

element 부모의 자식 중,  n번째 자식이 element 인 경우 선택, 아니면 선택X

element 부모의 자식 중,  element에 해당한 n번째  자식을 찾는다.