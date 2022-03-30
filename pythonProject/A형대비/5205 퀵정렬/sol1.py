'''
5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
'''
import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

def partition(left, right):
    if left >= right:
        return

    pivot = left
    i = left+1
    j = right-1
    while i <= j:
        while i <= j and A[pivot] >= A[i]: i += 1

        while i <= j and A[pivot] <= A[j]: j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]

    A[pivot], A[j] = A[j], A[pivot]

    partition(left, j)
    partition(j+1, right)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    left = 0
    right = len(A)
    partition(left, right)

    print(f'#{test_case} {A[N//2]}')