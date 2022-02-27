'''
4836_색칠하기
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr_info = [list(map(int, input().split())) for _ in range(N)]
    #color = 1 (빨강), color = 2 (파랑)
    matrix = [[0] * 10 for _ in range(10)]
    for n in range(N):
        if arr_info[n][-1] == 1:
            r1 = arr_info[n][0]
            c1 = arr_info[n][1]
            r2 = arr_info[n][2]
            c2 = arr_info[n][3]
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    matrix[i][j] += 1

        if arr_info[n][-1] == 2:
            r1 = arr_info[n][0]
            c1 = arr_info[n][1]
            r2 = arr_info[n][2]
            c2 = arr_info[n][3]
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    matrix[i][j] += 2

    cnt = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
    #pprint(matrix)

