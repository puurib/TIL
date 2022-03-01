import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 1001
    for _ in range(N):
        K, A, B = map(int, input().split())

        if K == 1:
            for i in range(A, B+1):
                cnt[i] +=1
        elif K ==2:
            for i in range(A, B, 2):
                cnt[i] += 1
            cnt[B] += 1
        else: # K==3
            for i in range()

    print(f'{tc} {cnt}')