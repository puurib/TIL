import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    arr_sum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            arr_sum = 0 # 매번 초기화
            for ii in range(i, i+M):
                for jj in range(j, j+M):
                    arr_sum+= arr[ii][jj]

            if max_sum <= arr_sum:
                max_sum = arr_sum


    print(f'#{tc} {max_sum}')