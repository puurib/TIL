

































import sys
sys.stdin = open('input.txt')


def bfs(si, sj, ei, ej):
    q = []
    visited = [[0] * N for _ in range(N)]

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if ci == ei and  cj == ej:
            return visited[ci][cj]-2


        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):
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