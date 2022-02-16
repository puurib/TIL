'''
GNS

해결 방식
1.

어려웠던 점
1.

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(str, input().split())
    k = int(K)
    input_arr = list(map(str, input().split()))
    arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dat = [0] * 10

    for idx in input_arr:
        for i in range(len(arr)):
            if idx == arr[i]:
                #print(arr[i])
                dat[i] += 1

    rlt = ''
    for i in range(len(arr)):
        rlt += (arr[i]+' ') * dat[i]

    print(f'#{tc} {rlt}')
