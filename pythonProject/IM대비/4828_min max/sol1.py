'''
4828_min max
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    rlt = max(arr) - min(arr)

    print(f'#{tc} {rlt}')
    #pprint(arr)

