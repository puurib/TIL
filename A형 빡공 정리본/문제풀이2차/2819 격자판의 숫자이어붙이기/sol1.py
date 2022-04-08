import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    print(f'#{tc} {arr}')
    for row in arr:
        print(row)