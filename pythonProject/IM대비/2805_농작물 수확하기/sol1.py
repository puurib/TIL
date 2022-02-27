'''
2805_농작물 수확하기 = 구간합
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(arr[0][N//2:N//2])

    cnt = 0
    for i in range(N):
        col = N//2
        arr[i][col-i:col+i]
        pass

    print(f'#{tc} {arr[0][col-1:col+1]}')
   #pprint(arr)

