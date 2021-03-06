# 개념은 중요치 않음, 구현을 할 수 있는가가 중요하다



# 후위표기법 (결과 똑같이 나오나 확인)

* 후위표기법은 중위에서 후위로 / 후위에서 계산하고 결과하는 두가지로 나눠진다.

* 숫자면 바로 결과로 가고, 숫자가 아닌 것들은 stack에 !

  ![image-20220224090802779](stack.assets/image-20220224090802779.png)

* 들어올 토큰과 이미 탑에 존재하는 토큰과 비교, 더 클때만 넣음

* 닫는 괄호가 icp일때, 여는괄호 만날때까지 팝해서 결과에 넣어줌

![image-20220224091311037](stack.assets/image-20220224091311037.png)

![image-20220224091457374](stack.assets/image-20220224091457374.png)

/랑 *랑 같으니까 같으면 *를 뱉어줘야함

![image-20220224091547863](stack.assets/image-20220224091547863.png)





## 연습문제1 -> 할수있으면 좋음, 못해도 괜찮음 (시뮬레이션 알고리즘 유형)

icp이 사실 가장 중요해서, 

![image-20220224092747658](stack.assets/image-20220224092747658.png)

큰것 부터 처리한다

![image-20220224092810315](stack.assets/image-20220224092810315.png)



## 계산기 (순서주의)

연산자를 만나면 숫자 두개를 꺼내서 계산하고 다시 결과를 넣음, 

반복..



![image-20220224100346260](stack.assets/image-20220224100346260.png)

![image-20220224100526461](stack.assets/image-20220224100526461.png)

## 내가 후위표현식을 보고 계산기라고 생각하고 계산하기

*  

![image-20220224100637180](stack.assets/image-20220224100637180.png)





## 백트레킹 (해를 찾는 도중에 막히면 다시 돌아가서 해를 찾는 기법)

![image-20220224101728854](stack.assets/image-20220224101728854.png)

* 1,4   1, 5  1,6, 까지 갔는데 갈때가없으니 다시 pop해서 다 빼주고 1,3이될때 이미 갔던 곳 말고 2,3으로 내려감 

![image-20220224102224702](stack.assets/image-20220224102224702.png)

![image-20220224102314973](stack.assets/image-20220224102314973.png)

* 백트레킹은 불필요한 경로를 차단한다.
  * DP는 풀이가 백트레킹과 다름, 이전 계산을 가지고 다음 계산을 함
  * 백트레킹은 dfs의 아류느낌, dfs에서 의미없는 길이면 차단해라고 조건문 돌리는 것

![image-20220224102414955](stack.assets/image-20220224102414955.png)

* dfs 에서 꼭 해보라고 한 코드? (알려달라하기)

``` python
def powerset(idx, N):

    if idx == N:  # 종료 조건
        print(bit)
        return

    bit[idx] = 1
    powerset(idx + 1, N)

    bit[idx] = 0
    powerset(idx + 1, N)


a = [0, 7, 2, 3]
N = len(a)
bit = [0] * N

powerset(idx=0, N=N)
```





## 상태 공간 트리

![image-20220224102719789](stack.assets/image-20220224102719789.png)





## 탐색이 줄어든다

![image-20220224102733848](stack.assets/image-20220224102733848.png)

## 연습문제 2번 (1번은 숙제가 아님)

1로 만들고 재귀호출, 0으로 만들고 재귀호출

재귀호출할 때 인덱스를 1증가해서 재귀호출

![image-20220224103400143](stack.assets/image-20220224103400143.png)



powerset코드

``` python
def powerset(idx, N):

    if idx == N:  # 종료 조건
        print(bit)
        return

    bit[idx] = 1
    powerset(idx + 1, N)

    bit[idx] = 0
    powerset(idx + 1, N)


a = [0, 7, 2, 3]
N = len(a)
bit = [0] * N

powerset(idx=0, N=N)
```



* 깊은 복사 : 1차원일땐 가능한 방법

![image-20220224103114551](stack.assets/image-20220224103114551.png)



* 여기서 시작

![image-20220224103150838](stack.assets/image-20220224103150838.png)



* 이번 인덱스의 자리를 0으로 만들고 인덱스를 하나 증가시키고

  

![image-20220224103221320](stack.assets/image-20220224103221320.png)

* 이번 인덱스의 자리를 1로만들고 또 인덱스 하나를 증가시킴

![image-20220224103246580](stack.assets/image-20220224103246580.png)



* 결론 (재귀함수를 이용한 완전탐색, DFS를 이용한 완전탐색 --> )

![image-20220224103741753](stack.assets/image-20220224103741753.png)

![image-20220224103811065](stack.assets/image-20220224103811065.png)

![image-20220224103754863](stack.assets/image-20220224103754863.png)



* dfs -> 1번 함수를 스택에 넣고, 
  * 함수의 콜스택 

![image-20220224103904528](stack.assets/image-20220224103904528.png)



## 부분집합

![image-20220224104306261](stack.assets/image-20220224104306261.png)

* 여기서 시작
* bit와 lst의 길이대로 원소별로 묶어줌(zip)
* each는 (1,2) (1,4)이렇게 들어감

![image-20220224104513248](stack.assets/image-20220224104513248.png)



![image-20220224104629071](stack.assets/image-20220224104629071.png)



잘짰나 확인해보기

![image-20220224104715995](stack.assets/image-20220224104715995.png)



---

![image-20220224104854261](stack.assets/image-20220224104854261.png)

![image-20220224104843131](stack.assets/image-20220224104843131.png)



* 부분집합 코드

![image-20220224105236525](stack.assets/image-20220224105236525.png)

![image-20220224105119955](stack.assets/image-20220224105119955.png)



* 12번 코드가 변화함
* 가지치기 코드를 넣으면 연산이 줄어듬 (필요없는 연산)

![image-20220224105749395](stack.assets/image-20220224105749395.png)



* 10이될것인데, 굳이 10 이 넘어가면 할필요가 없다.



![image-20220224105348423](stack.assets/image-20220224105348423.png)



* 이걸 짤 수 있는가 a형 단골문제 

![image-20220224105917940](stack.assets/image-20220224105917940.png)







---

* 순열 조합 (순서가 있는 열) 
  * 

![image-20220224110202049](stack.assets/image-20220224110202049.png)

* 함수에서 포문을 돌면서, 순서 바꾸고 재귀호출하고 원래대로 하기 (꼭 기억하기!!!!!!!!!!!) 
  * if문은 종료조건임.
  * ![image-20220224110410266](stack.assets/image-20220224110410266.png)
* 순열

![image-20220224110259064](stack.assets/image-20220224110259064.png)



* 순열 구하기

![image-20220224103310988](stack.assets/image-20220224103310988.png)

* 





## 퀵소트 (현재는 몰라도됨) cf) 바이너리 서치

* 분할정복알고리즘으로 바이너리 서치의 상위 개념이지만, 지금은 바이너리 서치만 알면됨

![image-20220224111017922](stack.assets/image-20220224111017922.png)



* 피봇이 중요하다 (pivot)

![image-20220224125155557](stack.assets/image-20220224125155557.png)



* 피봇을 두고 , 스타트 앤드를 둔다음, 한칸한칸 이동하면서 왼쪽오른쪽을 바꾼다는 개념

![image-20220224130103603](stack.assets/image-20220224130103603.png)

![image-20220224130139687](stack.assets/image-20220224130139687.png)





* 
* ![image-20220224130241351](stack.assets/image-20220224130241351.png)



* 파이써닉한 방법

![image-20220224130706421](stack.assets/image-20220224130706421.png)

터짐

오류 잡으면

![image-20220224130937049](stack.assets/image-20220224130937049.png)



* 파이써닉한 짧은것보다 파티션이 있는 코드가 더 중요함....!!!!!!!!!!!!!!!!!!!!!!



## 어제 유튜브라이브 

* 후위연산으로 어떻게 변경되는가 우리가원하는 결과로 어떻게 변경할 수 있는가?
* 파워셋 , 가지치기
* 퀵정렬

