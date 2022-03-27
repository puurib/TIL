


















'''
### 피자굽기

import sys
sys.stdin = open('input.txt')

def pizza(N, M, arr):
    q = []
    for i in range(1, N+ 1):
        q.append(i)  # 피자 번호 넣기

    idx = N + 1
    top = 0  # 피자번호 저장될 곳

    while q:
        top = q.pop(0)
        if arr[top] // 2 != 0:
            arr[top] //= 2
            q.append(top)

        elif idx <= M:
            q.append(idx)
            idx += 1

    return top


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [0] + list(map(int, input().split()))

    rlt = pizza(N, M, arr)
    print(f'#{tc} {rlt}')

### 미로의 거리
import sys

sys.stdin = open('input.txt')


def bfs(si, sj, ei, ej):
    q = []
    visited = [[0] * N for _ in range(N)]

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if ci == ei and cj == ej:
            return visited[ci][cj] - 2

        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and MAP[ni][nj] != '1':
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1

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

### 미로
from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    # queue.append([x,y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or miro[x][y] == 0):
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append((nx, ny))

    return miro[N - 1][M - 1]


print(bfs(0, 0))

### 유기농 배추
from collections import deque
import sys

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


def BFS():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 < nj < m and matrix[ni][nj] == 1:
                q.append([ni, nj])


T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    q = deque()

    for _ in range(n):
        if matrix[i][j] == 1:
            q.append([i, j])
            BFS()
            cnt += 1

    print(cnt)

### 바이러스
from collections import deque


def bfs(n):
    cnt = 0
    q = deque()
    visited[n] = True
    q.append(n)
    while q:
        V = q.popleft()
        for i in graph[V]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

    return cnt


computer = int(input())
number = int(input())
graph = [[] for _ in range(computer + 1)]
visited = [False for _ in range(computer + 1)]

for _ in range(number):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

rlt = bfs(1)

print(rlt)

### 노드의 거리
import sys

sys.stdin = open('input.txt')


def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        w = Q.pop(0)  # 다음 나오세요
        for i in range(V + 1):  # 노드의 개수 만큼 반복

            if field[w][i] == 1 and visited[i] == 0:
                # 연결된 다음 번호 큐에 넣기
                Q.append(i)  # w로 착각하면 안됨

                # 이전 방문 정보에 +1 == 이동한 거리
                visited[i] = visited[w] + 1
    if visited[G]:  # 골에 방문했다면?
        return visited[G] - 1
    else:  # 시작한 곳으로부터 다돌았는데 visited[G]이 0이라면 (도착x)
        return visited[G]  # 이러면 return 0 이랑 같음


T = int(input())
for tc in range(1, T + 1):

    V, E = map(int, input().split())
    #
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    # 방문 정보
    visited = [0] * (V + 1)  # 시작번호가 1이라서

    # 0으로 초기화 된 인접 행렬
    field = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    # 연결된 곳 1로 만들기
    for each in line:
        start = each[0]
        end = each[1]

        field[start][end] = 1
        field[end][start] = 1

    rlt = bfs(S)

    print(f'#{tc} {rlt}')
'''