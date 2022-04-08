'''
5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 D3
'''
# NxN의 미로가 주어진다. 최소 몇 개의 칸을 지나면 출발지에서 도착지까지 다다를지 알아내
# 경로 있으면 최소한의 칸수 / 경로 없으면 0 출력
# 1은 벽 / 0은 통로 / 2에서 출발해서 3에서 도착

import sys
from pprint import pprint
sys.stdin = open('input.txt')

def BFS(start):
    # [2] 델타 설정
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # [3] 큐 생성 후 초기값 삽입
    q = []
    q.append(start) # [i, j] 형태로 들어감

    # [4] q를 돌린다, 이때
    while q:
        i, j = q.pop()

        # [5] 여기서 방문처리를 해준다
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # [6] 범위 조건에 맞는지 확인한다
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:

                # [7] 통로라면,
                if arr[ni][nj] == 0:
                    # [8] visited 배열에 이전보다 1을 더한 값을 넣고
                    visited[ni][nj] = visited[i][j] + 1
                    # [9] q에 그 값을 넣는다.
                    q.append([ni, nj])

                # [10] 도착지점이라면
                elif arr[ni][nj] == 3:
                    return visited[ni][nj]
        return 0

T = int(input())

for tc in range(1, T + 1):
    # 5<=N<=100
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # [0] 체크할 visited 배열 만들어주자.
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # [1] 먼저 2(출발지 좌표를 찾음)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]



    
    print(f'#{tc} {BFS(start)}')
