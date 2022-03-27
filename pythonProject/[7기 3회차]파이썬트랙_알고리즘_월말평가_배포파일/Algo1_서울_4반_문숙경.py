T = int(input())


for tc in range(1, T + 1):
    # 싸피 왕국에는 N x N 크기의 당근 농장 , M 마리의 토끼
    N, M = map(int, input().split())
    # 토끼 정보 받아옴 [시작행, 시작열, 방향, 점프 거리]
    rabbit = [list(map(int, input().split())) for _ in range(M)]
    # 토끼의 방문 정보를 담을 배열 초기화
    arr = [[0] * N for _ in range(N)]

    # di, dj 상(0),하(1),좌(2),우(3)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    # 토끼 정보 rabbit에서 각각의 토끼마다 정보를 담아줌
    for r in rabbit:
        ii = r[0]
        jj = r[1]
        direction = r[2]
        jump = r[3]
        #print(ii, jj)

        arr[ii][jj] = 1  # 시작점은 무조건 1 찍기

        # arr을 순회하면서 시작점이 되는 때에,
        for i in range(N):
             for j in range(N):
                if i == ii and j == jj:
                    # 방향과 점프를 설정해주고
                    for p in range(0, N, jump):
                        ni = i + di[direction] * p
                        nj = j + dj[direction] * p
                        # arr 배열의 제한 구역 안에서만 1을 찍어줌
                        if 0 <= ni < N and 0 <= nj <N:
                            # 이 문제는 정확한 횟수를 요구하는 것이 아니라,
                            # 방문한 땅= 피해를 입은 구역만 찾고 있으므로 표시만 해줘도 됨
                            arr[ni][nj] = 1


    # arr의 1의 개수를 셀 변수 cnt
    cnt = 0

    # arr에서 1의 개수를 셈
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt +=1


    print(f'#{tc} {cnt}')

