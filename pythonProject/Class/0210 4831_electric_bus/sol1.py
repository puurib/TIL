'''
4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
# 0. T = tc의 개수, 정수의 개수 N과 구간의 개수 M,  numbers = N개의 양수
for tc in range(1, T + 1):
    n= int(input()) # 블럭의 개수 (가로 길이)
    data = list(map(int, input().split())) # 블럭 높이

    sum_data = [0] * n #낙차를 저장할 list

    # 1. 우측으로 나보다 작은 값의 개수 세기
    for idx in range(0, n-1):
        for idx2 in range(idx+1, n):
            if data[idx] > data[idx2]:
                sum_data[idx] += 1
    #print(sum_data)
    # 2. 1에서 가장 큰 값 출력
    for i in sum_data:
        if sum_data[0] < i:
            sum_data[0] = i
    print(f'#{tc} {sum_data[0]}')