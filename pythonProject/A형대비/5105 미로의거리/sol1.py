import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# BFS 선언
def BFS(point):
    # 스타트 지점 q에 넣고 시작
    q = deque()
    q.append(point)

    while q:
        i, j = q.popleft()
        # 4방향 탐색해서 방문하지 않았고 통로이면
        # 방문처리하고 1씩 증가
        # 도착 지점을 만나면 방문 값 반환
        # 도착 지점을 못 만나면 0 반환
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if matrix[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])
                elif matrix[ni][nj] == 3:
                    return visited[i][j]
    return 0

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 스타트 지점 찾기
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                start_point = [i, j]

    print(f'#{tc} {BFS(start_point)}')