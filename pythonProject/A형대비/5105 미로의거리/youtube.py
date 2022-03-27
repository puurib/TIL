from pprint import pprint
import sys
sys.stdin = open('input.txt')


def bfs(si, sj, ei, ej):
    q = [] # [0] 초기화
    visited = [[0] * N for _ in range(N)]

    q.append([si, sj])  # [1] Q에 초기데이터 삽입 방문 표시
    visited[si][sj] = 1

    while q:   # current
        ci, cj = q.pop(0)  # [2] Q에서 데이터 한개를 꺼냄
        if ci == ei and  cj == ej: # 가능한 경우 종료조건 처리
            return visited[ci][cj]-2


        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]): # [3] 조건에 맞는 경우 큐에 삽입, 방문처리
            ni, nj = ci+di, cj+dj
            if 0<= ni <N and 0<=nj <N and visited[ni][nj] ==0 and MAP[ni][nj] != '1':
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] +1

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == '2':
                si, sj = i, j
            elif MAP[i][j] == '3':
                ei, ej = i, j


    sol = bfs(si, sj, ei, ej)
    print(f'{tc} {sol}')
    #pprint(MAP)