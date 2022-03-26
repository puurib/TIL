from collections import deque

# 가로 세로 크기 변수 가져오기
N, M = map(int, input().split())
# 미로를 matrix로 받아오기
matrix = [list(map(int, input())) for _ in range(N)]
# 미로에서 간 거리를 count 행렬에 표시
count = [[0 for _ in range(M)] for _ in range(N)]
# 미로에서 방문했으면 방문 처리 행렬
visited = [[False for _ in range(M)] for _ in range(N)]

# 방향 벡터
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 시작지점을 queue에 담아서 표시
queue = deque([0, 0])
# 시작지점 방문 처리
visited[0][0] = True
# 시작지점을 거리 1로 보기
count[0][0] = 1

# bfs 시작
while queue:
    # bfs 시작을 꺼내기
    i, j = queue.popleft()

    # 종료 조건 도착지점을 만나면 while 더이상 돌지마
    if i == N-1 and j == M-1:
        break

    # 갈수있는 방향 체크하기 위해서 4방향 반복문
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        # 범위를 넘지 않고 방문하지 않았으며 통로인 구역이면 if 조건에 성립
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and matrix[ni][nj] == 1:
            # 갈 수 있는 곳이니까 queue에 담아주고
            # 방문처리
            # 한칸 진행했으니까 다음칸은 count += 1
            queue.append([ni, nj])
            visited[ni][nj] = True
            count[ni][nj] += count[i][j] + 1

# 시작지점을 1로 잡고 출발해서 -1을 해줌
print(count[N - 1][M-1])