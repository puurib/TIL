import sys
from pprint import pprint
sys.stdin = open('algo2_sample_in.txt')

def bfs(start): # 배열로 들어옴
    Q = [] # queue 생성

    dr = [-1, 1, 0, 0] # 상하좌우
    dc = [0, 0, -1, 1]

    area, cost = 0, 0

    visited[start[0]][start[1]] = 1
    Q.append(start)

    while Q: # [rr, cc] 형태로 큐에 들어감.
        # 맨 앞 나오세요.
        r, c = Q.pop(0)

        area += 1
        cost += matrix[r][c]

        for d in range(4):
            next_r = r + dr[d]
            next_c = c + dc[d]

            if 0 <= next_r < N and 0 <= next_c < N:
                if not visited[next_r][next_c] and matrix[next_r][next_c]:
                    Q.append([next_r, next_c])
                    visited[next_r][next_c] = 1


    return area, cost

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _  in range(N)]

    max_area, min_cost = 0, 9999999

    for r in range(N):
        for c in range(N):
            if not visited[r][c] and matrix[r][c]:
                area, cost = bfs([r, c])

                # 결과처리
                if area > max_area:
                    max_area = area
                    min_cost = cost
                elif area == max_area and cost < min_cost:
                    min_cost = cost

    print(f'#{tc} {max_area} {min_cost}')