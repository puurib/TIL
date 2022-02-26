import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):


            range_cnt = 0
        if i+K < N:
            range_cnt = arr[]

        # if max_cnt <= range_cnt:
        #     max_cnt = range_cnt

    print(f'#{tc} {range_cnt}')
    pprint(arr)

