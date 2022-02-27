'''
1979_어디에 단어가 들어갈 수 있을까
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check_lst = [1] * K
    rlt = 0
    check = ''
    # 가로
    for i in range(N):
        check = ''
        cnt = 0
        cnt = sum(arr[i][0:N])
        for j in range(N-K+1):
            if arr[i][j:j+K] == check_lst:
                check = 'y'
        if cnt == K and check == 'y':
            rlt += 1
    print(f'#{tc} {rlt}')


