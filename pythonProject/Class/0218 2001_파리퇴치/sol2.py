import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = []
    # 2차원 arr input 받기
    for row in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    max_sum = 0
    sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for ii in range(i, i+M):
                for jj in range(j, j+M):
                    sum += arr[ii][jj]

            if max_sum <= sum:
                max_sum = sum


    print(f'#{tc} {max_sum}')
