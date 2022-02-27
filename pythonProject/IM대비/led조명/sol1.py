'''
led조명 - 1차원리스트 & 그리디

[input.txt]
5 // 전체 Test Case 수
5 // 첫번째 Test Case의 N (LED 등 및 버튼의 수 )
1 1 0 0 1 // 원하는 LED 패턴 ( N개의숫자 )
6 // 두번째 Test Case의 N (LED 등 및 버튼의 수 )
0 1 1 1 0 0 // 원하는 LED 패턴 ( N개의 숫자 )
7
1 1 1 1 1 1 1
10
0 1 0 1 0 1 0 1 0 1
20
0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 1 1 0 0

[output.txt]
#1 3
#2 2
#3 1
#4 1
#5 8
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = [0]+list(map(int, input().split())) # 원하는 스위치의 상태 [0]을 더해줌 인덱스맞추려고
    lst = [0] * (N+1)
    cnt = 0

    for i in range(N+1):
        if i == 0: # arr[i] 이렇게하면 답안나옴..
            continue
        if arr[i] == lst[i]: # 같으면 넘어가!
            continue
        else: # arr[i] != lst[i]
            for j in range(i, N+1):
                if j % i == 0:
                    if lst[j]:
                        lst[j] = 0
                    else:
                        lst[j] = 1
            cnt += 1

        if lst == arr:
            print(f"#{tc} {cnt}")
            break
