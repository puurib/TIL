'''
1979_어디에 단어가 들어갈 수 있을까
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [[0]+ list(map(int, input().split()))+[0] for _ in range(N)]
    arr.insert(0, [0]* (N+2))
    arr.append([0] * (N+2))
    check_lst = [0]+([1] * K)+[0]
    rlt = 0

    # 가로
    for i in range(1, N+1):
        for j in range(N - K + 1):
            if arr[i][j:j + K+2] == check_lst:
                rlt += 1

    # 전치 행렬

    arr2 = list(map(list, zip(*arr)))
    for i in range(1, N+1):
        for j in range(N-K+1):
            if arr2[i][j:j+K+2] == check_lst:
                rlt += 1

    print(f'#{tc} {rlt}')



