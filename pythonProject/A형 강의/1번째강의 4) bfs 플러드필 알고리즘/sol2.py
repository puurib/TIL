def BFS(si, sj):
    distance_mat = [[0] * (4) for _ in range(4)]
    visited = []
    queue = [[si, sj]]

    # 선입선출
    while queue:
        # 현재 바라보는 좌표([ti, tj]): 큐의 맨 앞
        # 중복을 피해서 좌표를 방문 기록
        # tmp랑 '연결이 된 좌표들'을 큐에 더해줘요
        # 큐을 다시 꺼내가면서 큐이 다 빌때까지 순회를 해요.
        ti, tj = queue.pop(0)
        if [ti, tj] not in visited:
            visited.append([ti, tj])

            for d in range(4):
                ni = ti + di[d]
                nj = tj + dj[d]
                if 0 <= ni < 4 and 0 <= nj < 4 and [ni, nj] not in visited:
                    queue.append([ni, nj])
                    distance_mat[ni][nj] = distance_mat[ti][tj] + 1

    return distance_mat


matrix = [[0] * (4) for _ in range(4)]

# 델타 - 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for row in BFS(2, 3):
    print(row)