'''
5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 D3
'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    matrix = [[0] * N for _ in range(N)]

    # 오른쪽 아래쪽 이동
    di = [0, 1]
    dj = [1, 0]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                for k in range(2):
                    ni = i + di[k]
                    nj = j + dj[k]
                    r = []
                    while r >= 0 and r < N and c >= 0 and c < N:
                        matrix[r][c] = 1
                    if 0<= ni < N and 0<= nj <N:
                        r = [arr[ni][nj]] + r
                    if ni == N-1 and nj == N-1:
                        route.append(r)

    print(f'#{tc}')
    pprint(route)