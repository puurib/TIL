




























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