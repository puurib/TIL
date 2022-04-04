T = int(input())
for tc in range(1, T + 1):
    # 행의 개수 N과 열의 개수 M,사각 테두리 한 변의 크기 K
    N, M, K = map(int, input().split())
    # arr
    arr = [list(map(int, input().split())) for _ in range(N)]

    # max_cnt 변수 생성
    max_cnt = 0

    # 방향
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 시작값을 제어하려고 함
    for i in range(N-K+1):
        for j in range(M-K+1):
            visited = [[0 for _ in range(M)] for _ in range(N)]
            # cnt변수 생성
            cnt = 0
            # 배열탐색
            for k in range(K):
                for direction in range(4):
                    ni = i + di[direction] * k
                    nj = j + dj[direction] * k
                    # 조건 설정에서 도넛 모양 설정을 못함
                    if 0 <= ni < K and 0 <= nj <K:
                        cnt += arr[ni][nj]
                        #visited[ni][nj] += 1
            
            # max_cnt와 cnt를 비교하여 갱신
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')


