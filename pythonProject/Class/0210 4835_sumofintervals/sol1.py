'''
4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
# 0. T = tc의 개수, 정수의 개수 N과 구간의 개수 M,  numbers = N개의 양수
for tc in range(1, T + 1):
    N, M= map(int, input().split())
    numbers = list(map(int, input().split()))

    # N 개 중에 앞에서 M개 , 뒤에서 M개
    list_1 = numbers[0:M]
    list_2 = numbers[-M:]
    sum_1 = 0
    sum_2 = 0
    result = 0
    # 각 list의 합을 구함
    for i in list_1:
        sum_1 += i
    for i in list_2:
        sum_2 += i

    # 앞 뒤 list의 합에서, 차를 구함
    if sum_1 > sum_2:
        result = sum_1 - sum_2
    else:
        result = sum_2 - sum_1

    print(f'#{tc} {result}')