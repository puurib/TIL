'''
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
'''
from pprint import pprint
import sys, math
sys.stdin = open('input.txt')


def



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited 방문표시 일차원리스트로 충분
    visited = [0 for _ in range(N)]

    # rlt
    rlt = 100 * N
    # 1회차부터 시작,
    search(1, 0, 0)
    print(f'#{tc} {rlt}')