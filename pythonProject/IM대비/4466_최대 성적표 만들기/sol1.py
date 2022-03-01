'''
4466_최대 성적표 만들기
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    cut = lst[:M]
    rlt = sum(cut)
    print(f'#{tc} {rlt}')
