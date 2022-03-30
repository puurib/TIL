'''
5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    # rlt = quicksort(arr)
    print(f'{tc}')