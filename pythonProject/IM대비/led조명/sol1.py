'''
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
    arr = list(map(int, input().split())) # 원하는 스위치의 상태

    lst = [0] * N
    num = [i for i in range(1, N+1)]


    for i in range(N):
        if num[i] % i+1 == 0:  # arr[0] 을 1로 나눌때부터
            if lst[i] == 0:
                lst[i] = 1
            elif list[i] == 1:
                lst[i] == 0

    print(f'#{tc} {arr} {lst}')
    #pprint(arr)

