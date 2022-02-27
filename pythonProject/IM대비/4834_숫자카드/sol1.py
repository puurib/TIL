'''
4834_숫자카드
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    num_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = [0] * 10
    max_num = 0
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] in num_lst:
            cnt[arr[i]] += 1

    for j in range(len(cnt)):
        if max_num <= cnt[j]:
            max_num = cnt[j]
            max_idx = j

    print(f'#{tc} {max_idx} {max_num}')
    #pprint(arr)

