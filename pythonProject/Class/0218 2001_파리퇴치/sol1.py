'''
1859. 백만 장자 프로젝트

해결 방식
1.

어려웠던 점
1.

'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input()) # tc수 = 3

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    lst = []
    for row in range(N):
        row = list(map(int, input().split()))
        lst.append(row)

    # N-M+1까지 탐방하는 거같다.
    # sum이라는 합이 필요함
    max_sum = 0
    sum = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            # MxM
            sum = 0
            for i in range(row, row+M): # 시작위치 주의!!!
                for j in range(col, col+M): # 시작위치 주의!!!
                    sum += lst[i][j]

            if sum >= max_sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')






