# swea 1209 sum
'''
00X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
'''

import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = 10 # tc 개수
N = 100
#
for tc in range(1, T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0  # 최대값 초기화
    # 행의 합
    for i in range(N):
        sum_value = 0 # 행의 합 초기화
        for j in range(N):
            sum_value += arr[i][j]
        if sum_value > max_value:
            max_value = sum_value # 최대값 갱신

    # 열의 합
    for i in range(N):
        sum_value = 0 # 열의 합 초기화
        for j in range(N):
            sum_value += arr[j][i]
        if sum_value > max_value:
            max_value = sum_value # 최대값 갱신


    # 대각선 왼쪽 위 -> 오른쪽 아래
    sum_value = 0 # 이중 for문을 돌지 않음
    for i in range(N):
        sum_value += arr[i][i]
        if sum_value > max_value:
            max_value = sum_value # 최대값 갱신

    # 대각선 오른쪽 위 -> 왼쪽 아래
    sum_value = 0
    for i in range(N):
        sum_value += arr[i][N-1-i]
        if sum_value > max_value:
            max_value = sum_value  # 최대값 갱신

    print(f'{tc} {max_value}')