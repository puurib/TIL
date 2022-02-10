# 1206. [S/W 문제해결 기본] 1일차 - View
# 0~9 임의의 카드 6장을 뽑았을 때 3장의 카드 연속 - run, 동일한 번호- triplet

import sys
sys.stdin = open('input.txt')
#
T = int(input())

for tc in range(10):
    arr = [0] * T
    data = list(map(int, input().split()))
    for i in range(T-1):
        if data[i] - data[i+1] >= 1:


        print(f'#{tc} 0')


