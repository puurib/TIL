# swea 1954. 달팽이 숫자
'''
10
1
2
3
4
5
6
7
8
9
10
'''

import sys
sys.stdin = open('input.txt')

T = int(input()) # tc 개수 = 10개

#
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    d = 0 # 방향
    r = 0 # 행 좌표
    c = 0 # 열 좌표
    num = 1 # 내가 찍을 숫자

    dr = [0, 1, 0, -1]  # dr, dc는 달팽이 모양 순서대로 서술
    dc = [1, 0, -1, 0]
    # arr
    while num <= N * N:
        arr[r][c] = num
        num += 1

        # (0,0) -> (0,1) -> (0,2) -> ... -> (N,N)
        nr = r + dr[d]
        nc = c + dc[d]

        # 유효한 좌표인지 검사
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f'{arr[i][j]}', end=' ')
        print()