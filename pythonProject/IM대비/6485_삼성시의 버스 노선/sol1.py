'''
6485_삼성시의 버스 노선
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) #N 노선수
    cnt = [0] * 5001

    AB = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    P_lst = []
    for _ in range(P):
        P_lst.append(int(input()))

    for i in range(N):
        for j in range(int(AB[i][0]), int(AB[i][1])+1):
            cnt[j] += 1

    # 버스 노선 수가 중복....!!!!
    print(f'#{tc}', end= ' ')
    for x in P_lst:
        print(cnt[x], end=' ')
    print()


