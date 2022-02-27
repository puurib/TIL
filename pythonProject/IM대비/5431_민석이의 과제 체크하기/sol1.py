'''
5431_민석이의 과제 체크하기
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))
    check_lst = [0] * N

    for i in range(K):
        idx = arr[i]
        check_lst[idx-1] = 1

    zero_lst= []
    for i in range(len(check_lst)):
        if check_lst[i] == 0:
            zero_lst.append(i+1)
    print(f'#{tc}', end =' ')
    print(*zero_lst)
    #pprint(arr)

