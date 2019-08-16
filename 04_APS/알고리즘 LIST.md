# 알고리즘 LIST1

## 기본1. 배열(Array) 1

* 알고리즘 문제 풀이 방법
  1. 요구사항선택
  2. 설계
  3. 구현
  4. 테스트
  5. 유지보수

* 알고리즘의 성능은 시간복잡도 = 빅-오 표기법으로 측정한다.

이때, 최고차항에 계수를 생략하여 표시한다.

---

ex)

P(Polynomial time)
$$
O(log n)  : 이진탐색
$$

- 기본적으로 정렬이 된 상태에서 1부터 100사이 숫자 up,down으로 찾는 과정 => log100 => 6~7번 사이에 찾을 수 있다.

$$
O(n) : 순차탐색
$$

$$
O(nlogn) : 퀵소트, 병합, heap
$$

---

NP(Non-deterministic Polynomial time) : 개발에는 사용 못함
$$
O(n^2) : 선택, 버블, 삽입 정렬
$$

$$
O(n!) : 순열
$$

---

* 완전 검색(Exaustive Search)

문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법

우선, 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다. 즉, 가지치기를 해라

완전검색에 가지치기하는 것을 백트래킹이라고 한다.

완전검색은 재귀로 하는 방법을 알아야 된다.

---

* 탐욕(Greedy) 알고리즘

근시안적인 방법.

거스름돈 줄이기 : 만일 400원짜리 동전이 생긴다면, 400원짜리 동전 2개로 800원을 낼 수 있다.

즉, 단위가 큰 동전으로만 만들면 동전의 개수가 줄어든다는 것은 Greedy한 알고리즘이다.

지역적으로 최적으로 만든다고 해서 전체적으로 봤을 때 최적이지는 않는다. 그러니까 완전검색을 해라.

---

* 램

code: 함수 실행

data : 전역변수

heap : 리스트, 배열

stack : 변수; 만일 재귀호출하면 변수가 스택에 쌓임

---

* 버블 정렬 (Bubble Sort)

인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

정렬 과정 :

​	첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.

​	한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.

​	교환하며 자리를 이동하는 모습이 물 위에 올라오는 버블과 모양이 같다.

​	정렬할 리스트의 원소 개수 - 1 번 for문을 돌리면 된다.
$$
시간 복잡도: O(n^2)
$$
바깥번째 까지 for문을 작성하고 싶다면

거꾸로 떨어지는 포문을 바깥에 작성한다

```Python
def BubbleSort(a) :
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```

swap 함수 => temp를 이용해서 변수에 값을 바꾼다.

---

* 카운팅(Counting Sort)

항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

ASCII

0~127

65 = 'A', 97 = 'a'

배열 자체를 인덱스로 사용하여 카운트를 만들고, 이를 (인덱스-1)로 사용하여 카운팅소트에 이용.

## 01_workshop

## 기본2. 배열(Array) 2

* 2차원 배열 선언 방법 2가지

```python
# 1번째 방법
   # data = [[0 for in range(col)] for in range(row)]
   # for i in range(row):
   #     data[i] = list(map(int, input().split()))
# 2번째 방법
   #data = [list(map(int, input().split())) for _ in range(row)]
```

* 행 우선 순회 

```
for i in range(len(Array)):
	for j in range(len(Array[i])):
		Array[i][j]
```

* 열 우선 순회: 행 우선 순회에서  j<->i 순서만 바꾸면된다.

```
for i in range(len(Array)):
	for j in range(len(Array[i])):
		Array[j][i]
```

* 델타 탐색

4방향을 탐색

```
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for x in range(len(ary)):
	for y in range(len(ary)):
		for I in range(4):
			testX = x + dx[I]
			testY = y + dy[I]
			test(ary[testX][testY])
```

* 전치 행렬

```
for i in range(3):
	for j in range(3):
		if i < j:
			arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
#----------------------
for i in range(3):
	for j in range(i+1,3):
		arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

방향성이 없는 그래프에서 반만 구하고 전치 행렬로 복사하면 된다.

---

* 부분집합

```
def printList(data, bit):
	for i in range(len(bit)):
		if bit[i]: print(data[i], end=" ")
	print()
	
data = [1,2, 3]
bit = [0, 0, 0]
	for i in range(2):
		bit[0] = i
			for k in range(2):
				bit[2] = k
				printList(data, bit)
```

재귀로 해야된다

이렇게 for문으로하면 가지치기가 불가능하다.

---

* 비트연산자

1.  ^ : xor을 2번반복하면 원래상태로 돌아온다.

2.  _ << 1 :  2곱하기를 뜻함 /   _ >> 1  : 2나누기를 뜻함

ex) 8 >> 3 은 1를 뜻함.

3. i & (1<< j ) : 숫자 i의  j 번째 비트가 1인지 아닌지를 리턴한다.

ex)  6 = 0110

6 & (1<<0 ) -> 0

6 & (1<<1 ) -> 1

6 & (1<<2 ) -> 1

6 & (1<<3 ) -> 0

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(1<<n) :
    for j in range(n+1):
        if 1 & (1 << j):
            print(arr[j, end=", "])
     print()
```

---

* 검색

순차검색

* 이진검색

자료의 가운데를 본고 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

이전 검색은 자료가 정렬된 상태여야 한다.

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해 새로 검색을 수행. 크다면 반대.
4. 반복

```
def binarySearch(a, key):
	start = 0
	end = len(a) - 1
	while start <= end:
		middle = (start + end) // 2
		if key == a[middle]:
			return middle
		elif key < a[middle]:
			end = middle - 1
		else:
			start = middle + 1
	return -1
key = 19
data = [2,4,7,9,11,19,23]
print(binarySearch(data, key))
```

---

* 인덱스
* 셀렉션
* 선택정렬

> > 