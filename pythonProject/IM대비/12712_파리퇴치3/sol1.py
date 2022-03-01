'''
1221_GNS dat문제
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N= 배열크기, M= 파워크기
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 가로 세로
    max_sum = 0
    r = [-1, 1, 0, 0]
    c = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            each_sum = arr[i][j]
            for d in range(len(r)):
                for p in range(1, M):
                    ii = i + r[d] * p # 파워
                    jj = j + c[d] * p # 파워
                    if 0<= ii < N and 0<= jj <N:
                        each_sum += arr[ii][jj]
            if max_sum <= each_sum:
                max_sum = each_sum

    # 대각선
    r1 = [-1, -1, 1, 1]
    c1 = [-1, 1, 1, -1]
    for i in range(N):
        for j in range(N):
            each_sum1 = arr[i][j]
            for d in range(len(r1)):
                for p in range(1, M):
                    ii = i + r1[d] * p  # 파워
                    jj = j + c1[d] * p  # 파워

                    if 0<= ii < N and 0<= jj <N:
                        each_sum1 += arr[ii][jj]
            if max_sum <= each_sum1:
                max_sum = each_sum1

    print(f'#{tc} {max_sum}')



