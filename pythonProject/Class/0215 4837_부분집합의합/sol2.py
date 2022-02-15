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

sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 12개의 숫자를 원소로 가지는 집합 A 이므로 range를 13으로 줌
    arr = [int(i) for i in range(1, 13)]

    cnt = 0
    for i in range(1<<len(arr)):
        subset_lst = []                     # 빼내온 부분집합을 집어넣을 리스트
        sub_sum = 0                       # 부분집합의 합을 구해야 하므로 변수
        for j in range(len(arr)):
            if i & (1 << j):                # i의 부분집합일 때,
                subset_lst.append(arr[j])     # 부분집합 리스트에 더해주고
                sub_sum += arr[j]           # 해당 부분집합을 더해주는 값을 도출
        if len(subset_lst) == N and sub_sum == K:     #총 원소 수가 N이고, 원소의 합이 K인 숫자인 경우
            cnt += 1                                    # 카운트를 올려준다

    print(f'#{tc} {cnt}')
