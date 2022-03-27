T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방향 정보
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, -1, 1, -1, 1]
    # 땅 가격, 면적 cnt
    cnt = []
    # info 땅이 있는 곳 좌표 구하기 - bfs로 풀어야하는데..
    info = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                info.append((i,j))
                ddang = 0
                money = 0
                for k in range(8):
                    ni = i + di[k] * N
                    nj = j + dj[k] * N

                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                        ddang += 1
                        money += arr[i][j]
                        cnt.append([ddang, money])

    print(f'#{tc} {N}')


