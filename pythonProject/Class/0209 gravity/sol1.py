# gravity
# 상자가 오른쪽으로 90도 회전했을 때, 가장 큰 낙차값을 구함.
# 상자의 높이가 주어진다.
'''
T = 3

tc의 개수 = 9
tc = 7 4 2 0 0 6 0 7 0
tc의 개수 = 9
tc = 7 4 2 0 0 6 7 7 0
tc의 개수 = 20
tc = 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
# 0. T = tc의 개수, n = 몇개의 원소를 받을 것인가? data = 실제로 받은 값들
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