# HTTP 기초

웹서비스 : 요청(주소 URL 을 통해서)과 응답(문서 : THML, XML,  Json 등)

HTTP(hypertext transfer protocol)

HTTP 기본 속성 : 

1. Stateless : 상태정보가 저장되지 않음. 즉, 요청 사이에는  연결고리가 없음. 클라이언트가 서버와 상호작용하기 위해서 HTTP 쿠기를 만들고, 상태가 있는 세션을 활용할 수 있도록 보완

2. Connectless : 서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐

URL(Uniform Resource Location)

URI(Uniform Resource Identifier) : 어떻게 식별할 것 인가.

---

Scheme / Protocol | Host     |  Port  | Path

http://                       localhost   :3000  /posts/3

​                                               Query

http://google.com/search?q=http

​																							fragment

http://getbootstrap.com/docs/4.1/layout/overview#containers

​	

---

HTTP Method

GET : 지정 리소스의 표시를 요청하며, 오직 데이터를 받기만 함.

POST : 클라이언트 데이터를 서버로 보냄

PUT/PATCH : 서버로 보낸 데이터를 저장/지정 리소스의 

DELETE :

---

* RESTful

(Representational State Transfer)

* REST API

웹의 장점을 활용하는 것에 대한 철학(생각), 자원과 행위를 잘 표현 하자는 철학(생각) or 설계

* REST 구성

자원 URI / 행위 HTTP Method / 표현 Representations

* REST 특징

Cacheable(캐시가능) : HTTP의 캐시 기능이 적용 가능함

* REST 중심 규칙

1. URI은 정보의 자원을 표현해야 한다.
2. 자원에 대한 행위는 HTTP Method 로 표현한다.