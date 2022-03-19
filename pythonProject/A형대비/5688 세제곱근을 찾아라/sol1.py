'''
5688. 세제곱근을 찾아라 D3
'''
import sys, math

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    rlt = round(pow(N, 1 / 3), 2)
    if rlt != int(rlt):
        rlt = -1

    ans = int(rlt)
    print(f'#{tc} {ans}')