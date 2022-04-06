# A형 강의

## 문제 푸는 과정은 이해(N값 추론) 설계(tc로 단계별로 설계) 구현(코드 구현) 디버깅

![image-20220405185815240](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405185815240.png)

![image-20220405190255806](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405190255806.png)

## DFS : n의 값이 1~30이면, BFS: n이 2차원이고 50~200이면 가능성이 높음

![image-20220405185829513](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405185829513.png)



## 구현테스트 3가지

### 1. 리스트를 만들어서 수를 for문으로 돌려 채움

![image-20220405190436709](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405190436709.png)

```python
# easy버전 구현력
# 리스트를 만들어서 수를 포문 돌려서 채움
# 55 44 33 22 11 0

list = []

for i in range(5, -1, -1):
    list.append(i*11)

print(list)
```




### 2. 중복제거후 소팅

![image-20220405190455137](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405190455137.png)

``` python
# 중복을 제거 하고 알파벳 순서대로 출력

lst= ['A', 'B', 'T', 'A', 'A', 'A', 'B', 'A', 'A']

lst = list(set(lst))

lst.sort()
print(lst)
```





### 3. 재귀호출 (10, 9, 8, 7, 6, 6, 7, 8, 9, 10이렇게 나오도록)

![image-20220405190607876](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405190607876.png)

![image-20220405190705669](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405190705669.png)

``` python
# 순서 10, 9, 8, 7, 6, 6, 7, 8, 9, 10

def num(n):
    if n == 5:
        return
    print(n, end=' ')
    num(n-1)
    print(n, end=' ')
```







---

# BFS

리스트 자료구조에서 저장할 수 있는 최소칸을 노드라고 부름

값들을 어떻게 저장하고, 읽고 쓰고 관리할까?

리스트에 넣을까? 그래프에 넣을까? 연결리스트에넣을까 등등을 고민함.



![image-20220405191328329](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405191328329.png)





### 그래프를 탐색하는 방법 두가지가 BFS DFS

탐색 : 자료구조를 뒤지는 걸 탐색이라고 부름

리스트, 연결리스트는 for로 탐색하지만

그래프는 for로 탐색하기가 힘들다. 

그래서 그래프를 탐색하는 방법이 두가지가 있는데, 그게 바로 BFS DFS이다.

![image-20220405191602790](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405191602790.png)





----

#### 2차원배열에서 퍼지는 알고리즘 = 플러드필 알고리즘 

![image-20220405192007203](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405192007203.png)

이렇게 배열을 값으로 채워나가는 것을 플러드필 알고리즘이라고 부른다.

BFS의 일종임.

![image-20220405191652574](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405191652574.png)



* 능숙도 테스트

### 문제

![image-20220405193204536](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405193204536.png)



#### 1. 1을 중심으로 퍼트리기(훈련하기)

![image-20220405192510180](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405192510180.png)

![image-20220405193051490](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405193051490.png)





#### 2. 1이 3개가 있고 2, 3을 넣기 

![image-20220405193406772](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405193406772.png)

![image-20220405193602121](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405193602121.png)

초기값이 [(0, 3), (1, 1), (3, 3)]



#### 3. BFS 응용 : 천지창조 문제

![image-20220405193801116](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405193801116.png)

빨간 박스는 고정 

등록할 때마다 카운팅하면 크기를 구할 수 있음

![image-20220405193848020](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405193848020.png)



#### 4. 섬 몇개 ? (5분컷)

![image-20220405193934817](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405193934817.png)



이중 for문을 돌려서 섬하나(한칸)를 찾음

bfs를 돌려서 섬을 제거함



![image-20220405194214499](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405194214499.png)





#### 5. 미로찾기

![image-20220405194420334](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405194420334.png)![image-20220405194452854](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405194452854.png)



0부터 채워나가서 발견되면 해당 값 출력





#### 6. A->B->C 최단거리로 가기 = 미로찾기 두번하기 A->B / B->C (5분컷)

![image-20220405194750808](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405194750808.png)![image-20220405194728623](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405194728623.png)



#### 7. 





#### 미생물관찰 문제 D2

섬 개수 문제 (4번)

섬의 크기를 각각 수해서 max값 갱신



![image-20220405195211535](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405195211535.png)

![image-20220405195417813](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405195417813.png)

![image-20220405195425889](BFSDFS%20%EB%AC%B8%EC%A0%9C%20%EB%AA%A8%EC%9D%8C.assets/image-20220405195425889.png)