import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    rlt = max(arr) - min(arr)
    print(f'{tc} {rlt}')