'''
4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램

해결 방식
1.

어려웠던 점
1.

[input.txt]
3
3 6
5 15
5 10

[]
부분 집합은 2^n개이다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 부분집합 원소의 수 N(그래서 1~N까지)과 부분 집합의 합 K
    N, K = map(int, input().split())

    # arr 생성
    arr = []
    for i in range(1, N+1):
        arr.append(i)
    print(arr)





    # print(1<<N) # 8 32 32

        

    #print(f'{N} {K}')

