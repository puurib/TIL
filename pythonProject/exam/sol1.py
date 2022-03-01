import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_zero = 0 # 0 총 개수 구하기
    idx_i = 0 # 경비원의 위치
    idx_j = 0
    for i in range(N):
        for j in range(N):
            # 0 총 개수 구하기
            if arr[i][j] == 0:
                total_zero += 1
            # 경비원 위치 구하기
            if arr[i][j] ==2:
                idx_i = i
                idx_j = j

    see_zero = 0 # 경비원이 보이는 0
    r = [-1, 1, 0, 0]
    c = [0, 0, -1, 1]

    for d in range(len(r)):
        ii = idx_i + r[d]
        jj = idx_j + c[d]
        if 0<= ii < N and 0<= jj< N:
            n = 0
            while n >= N:
                if arr[ii][jj] == 0:
                    see_zero += 1
                elif arr[ii][jj] == 1:
                    break
                n += 1
                ii = idx_i + r[d] * n
                jj = idx_j + c[d] * n


    print(f'#{tc} {see_zero}')
    pprint(arr)

