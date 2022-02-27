'''
4843_특별한 정렬
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    f_arr = arr[:(N//2)]
    b_arr = arr[N//2:]
    b_arr.reverse()

    rlt = []
    for i in range((N//2)):
        rlt.append(b_arr[i])
        rlt.append(f_arr[i])


    print(f'#{tc}', end =' ')
    print(*rlt[0:10])
    #pprint(arr)

