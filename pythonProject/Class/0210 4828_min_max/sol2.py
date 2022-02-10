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

    # 1번 째 풀이 순서 1. 버블 정렬 -> 2. 차를 구한다. (메모리초과)

    # 1. for문을 하나를 쓰고, max, num를 그 안에서 구한다.
    max = numbers[0]
    min = numbers[0]
    result = 0
    for num in numbers:
        if max < num:
            max = num
        if num < min:
            min = num
    # 2. max - min
    result = max - min
    print(f'#{tc} {result}')