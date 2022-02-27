'''
1221_GNS dat문제
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = input().split()
    arr = list(input().split())
    dat =["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt =[0] * 10

    for i in range(int(M)):
        for j in range(len(dat)):
            if arr[i] == dat[j]:
                cnt[j] += 1

    lst = []
    for i in range(len(cnt)):
        idx = cnt[i] * (dat[i]+' ')
        lst.append(idx)

    print(f'{N}', end=' ')
    print(*lst)

