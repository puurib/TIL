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
    half = N // 2
    cnt = 0
    for i in range(N//2): # 반으로 잘라!

        cnt+= sum(arr[i][half-i:half + i+1])
        cnt+= sum(arr[N-1-i][half-i:half +i+1])

    cnt+= sum(arr[half])

    print(f'#{tc} {cnt}')
   #pprint(arr)

