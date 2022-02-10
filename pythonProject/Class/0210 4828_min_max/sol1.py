'''
4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
# 0. T = tc의 개수, N = 첫 줄에 양수의 개수  numbers = N개의 양수
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 풀이 순서 1. 버블 정렬 -> 2. 차를 구한다.

    result = 0
    for i in range(len(numbers) - 1):
        for j in range(i):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    result = numbers[0] - numbers[-1]
    print(f'{result}')