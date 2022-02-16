'''
swea 1210_ladder1

해결 방식
1.

어려웠던 점
1.

'''

import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 테스트 케이스
T = 10

# 테스트 케이스 만큼 입력 받기
for test_case in range(1, T + 1):
    data = []
    N = int(input())
    result = 0
    for _ in range(100):
        data.append([0] + list(map(int, input().split())) + [0])

    # start, end point 선언
    i = 99
    j = data[99].index(2)

    while True:
        if i == 0:
            break

        # 좌 조건 및 위 조건 나올때 까지 진행
        if data[i][j - 1] == 1:
            while True:
                j -= 1
                if data[i][j - 1] == 0:
                    break

        # 우 조건 및 위 조건 나올때 까지 진행
        elif data[i][j + 1] == 1:
            while True:
                j += 1
                if data[i][j + 1] == 0:
                    break

        # 위 조건 및 좌우 조건이 아니면 위로 진행
        i -= 1

    # 출력
    print(f'#{test_case} {j - 1}')