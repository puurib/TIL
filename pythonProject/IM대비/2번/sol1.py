'''
[output.txt]
#1 1
#2 18
#3 25
#4 90
#5 44
#6 62
#7 55
#8 119
#9 112
#10 224
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1번 3x3배열 : 그 원소 자기자신, 상하좌우, 대각선 (이 때 하나라도 벗어나면 0이됨)
    r = [0, -1, 1, 0, 0, -1, 1, 1, -1]
    c = [0, 0, 0, -1, 1, 1, 1, -1, -1]
    max_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            each_sum = 0
            for d in range(len(r)):
                ii = i + r[d]   # 그냥 d라고 쓰니까 안되지 바보야 으이구
                jj = j + c[d]   # 그냥 d라고 쓰니까 안되지 바보야 으이구
                if 0 <= ii < N and 0 <= jj < N:
                    each_sum += arr[ii][jj]
                else:
                    each_sum = 0
                    break

            if max_sum <= each_sum:
                max_sum = each_sum

    # 2번 크로스 *  파워
    max_sum2 = 0
    r = [-1, 1, 0, 0]
    c = [0, 0, -1, 1]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            each_sum2 = 0
            each_sum2 += arr[i][j]
            for d in range(len(r)):
                for p in range(1, arr[i][j]): # 원점은 위에 더해줌 그래서 1부터
                    ii = i + (r[d] *p)
                    jj = j + (c[d] *p)

                    if 0 <= ii < N and 0 <= jj < N:
                        each_sum2 += arr[ii][jj]

            if max_sum2 <= each_sum2:
                max_sum2 = each_sum2

    print(f'#{tc} {max_sum} {max_sum2}')
    #pprint(arr)

