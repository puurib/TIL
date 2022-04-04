import sys
sys.stdin = open('algo1_sample_in.txt')
T = int(input())

for tc in range(1, T + 1):
    # N은 행렬의 크기, M은 토끼의 수
    N, M = map(int, input().split())

    # N*N matrix
    matrix = [[0] * N for _ in range(N)]

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for _ in range(M): # 각각의 토끼마다
        r, c, direction, jump = map(int, input().split())

        # 각 토끼가 같은 방향 (dr/dc[direction])으로 가는데, 뛰어넘기(jump)
        while 0 <= r < N and 0 <= c < N:
            matrix[r][c] = 1 # 영역 표시

            # 점프하기
            r = r + dr[direction] * jump
            c = c + dc[direction] * jump

    cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                cnt += 1

    print(f'#{tc} {cnt}')
