'''
1210_Ladder1
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] + list(map(int, input().split()))+ [0] for _ in range(100)] # 쿠션 생성

    # 탐색
    # start, end point 선언
    i = 99
    j = arr[99].index(2) #2의 값이 있는 인덱스 찾기

    while True:
        if i == 0:
            break

        # 좌 조건 및 위 조건 나올때 까지 진행
        if arr[i][j - 1] == 1:
            while True:
                j -= 1
                if arr[i][j - 1] == 0:
                    break

        # 우 조건 및 위 조건 나올때 까지 진행
        elif arr[i][j + 1] == 1:
            while True:
                j += 1
                if arr[i][j + 1] == 0:
                    break

        # 위 조건 및 좌우 조건이 아니면 위로 진행
        i -= 1

        # 출력
    print(f'#{tc} {j - 1}')

