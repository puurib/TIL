import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    arr = [list(map(int, input())) for _ in range(5)]
    print(f'#{tc}')
    print(sum(arr[1][5 //2-1 : 5 // 2+2 ]))
    pprint(arr)

