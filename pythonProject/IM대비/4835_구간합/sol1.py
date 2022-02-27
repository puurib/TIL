'''
4835_구간합
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M= map(int, input().split())
    arr = list(map(int, input().split()))

    sum_num = [0] * (N-M+1)
    for i in range(N-M+1):
        sum_num[i] = sum(arr[i:i+M])

    rlt = max(sum_num) - min(sum_num)

    print(f'#{tc} {rlt}')
    #pprint(arr)

