# A형 강의(3번째, DFS)

![image-20220411194856816](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411194856816.png)

* 완탐은 for문과 재귀로 구현하기도 함 (완탐이 상위 종류라고 보면 됨)
  * 비밀번호 4자리의 자전거 자물쇠 찾기 : 4중 for문
  * ![image-20220411194955314](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411194955314.png)
  * N 자리?  재귀로 짜야함



* 그렇다면?

![image-20220411195057495](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411195057495.png)

이경우에는 for문을 써야할까? 재귀를 써야할까?

둘 다가능하지만 이 경우에는 8중 for문을 쓰면 됨



![image-20220411195140555](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411195140555.png)

이렇다면 재귀로.. 숫자가1~3인거고 N장이니깐 

for문이 몇개인지 모름

![image-20220411200507101](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411200507101.png)



---

## 그래프 탐색

1 탐색한다, 큐에서 뺀다

2 다음 갈곳을 예약한다

![image-20220411201846400](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411201846400.png)



![image-20220411202116355](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411202116355.png)



![image-20220411202210321](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411202210321.png)



## DFS

![image-20220411203459783](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411203459783.png)



> 1. 모든 노드 1회씩 탐색
>
> ![image-20220411203256935](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411203256935.png)
>
> 2. 모든 경로를 탐색 
>
> ![image-20220411203218656](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411203218656.png)





## BFS : 최단거리 알고리즘 (최소 몇회 이동?)

## (모든 경로를 다 탐색하는건 가능하긴 한데 메모리 낭비가 너무 심함 비추) 

![image-20220411203619825](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411203619825.png)



* bfs는 중간에 끊을 수 있음 한번만에 가는 경로 다 찾고, 그다음 찾고 그런식이여서
* dfs는 중간에 끊으면 안됨, 확신할 수 없음

* 다익스트라(최단거리) --> 벽뿌시기는 다익스트라가 더 빠름



---

## 문제 ![image-20220411205632453](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411205632453.png)14193 통신병 민코씨

![image-20220411210014917](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210014917.png)

* 

![image-20220411210142702](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210142702.png)

![image-20220411210211136](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210211136.png)

최소 신장 트리

![image-20220411210446710](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210446710.png)

![image-20220411210606642](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210606642.png)

![image-20220411210507072](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210507072.png)

![image-20220411210346595](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210346595.png)

![image-20220411210318300](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210318300.png)





## 다리만들기 17472

![image-20220411210700116](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210700116.png)



좌표알아내서 최단거리 그래프 만들고 MST하면 정답이 나옴

![image-20220411210839229](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210839229.png)







---

---

## used 배열 ![image-20220411210920610](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411210920610.png)



## 안나와 엘사 문제

안나는 상하좌우 가만히 쉬기 5방향

엘사는 대각선 4방향

---

![image-20220411211724624](A%ED%98%95%20%EA%B0%95%EC%9D%98(3%EB%B2%88%EC%A7%B8,%20DFS).assets/image-20220411211724624.png)





## url.kr/6vgqtn

