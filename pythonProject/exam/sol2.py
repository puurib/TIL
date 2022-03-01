import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_zero = 0
    idx_i = 0
    idx_j = 0
    for i in range(N):
        for j in range(N):

            if arr[i][j] == 0:
                total_zero += 1

            if arr[i][j] == 2:
                idx_i = i
                idx_j = j

    see_zero = 0
    t_i, t_j = idx_i,idx_j
    b_i, b_j = idx_i,idx_j
    l_i, l_j = idx_i,idx_j
    r_i, r_j = idx_i,idx_j

    r = [-1, 1, 0, 0]
    c = [0, 0, -1, 1]


    while t_i >= 0:
        if 0<= t_i - 1 <N and 0<= t_j <N:
            if arr[t_i-1][t_j] == 0:
               see_zero += 1
            elif arr[t_i-1][t_j] == 1:
                break
        t_i -= 1



    while b_i < N:
        if 0 <= b_i + 1 < N and 0 <= b_j < N:
            if arr[b_i + 1][b_j] == 0:
                see_zero += 1
            elif arr[b_i + 1][b_j] == 1:
                break
        b_i += 1


    while r_j >= 0:
        if 0 <= r_i< N and 0 <= r_j-1 < N:
            if arr[r_i][r_j-1] == 0:
                see_zero += 1
            elif arr[r_i][r_j-1] == 1:
                break
        r_j -= 1


    while l_j < N:
        if 0 <= l_i < N and 0 <= l_j + 1 < N:
            if arr[l_i][l_j + 1] == 0:
                see_zero += 1
            elif arr[l_i][l_j + 1] == 1:
                break
        l_j += 1

    rlt = total_zero - see_zero
    print(f'#{tc} {rlt}')