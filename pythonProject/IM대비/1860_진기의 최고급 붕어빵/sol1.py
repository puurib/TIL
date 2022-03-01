'''
1860_진기의 최고급 붕어빵
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    # N명의 사람이 자격을 얻었다.
    # 진기는 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    result = "Possible"

    # x초까지 만들어진 붕어 개수: (x // M) * K
    for i in range(N):
        boong = (lst[i] // M) * K - (i + 1)
        if boong < 0:
            result = "Impossible"
            break

    print("#{} {}".format(tc, result))

