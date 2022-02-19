import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    max_sum = 0
    # 1 기본 행
    for i in range(100):
        sum_ = 0
        for j in range(100):
            sum_ += arr[i][j]

        if max_sum >= sum_:
            max_sum = sum_

    for j in range(100):
        sum_ = 0
        for i in range(100):
            sum_ += arr[i][j]

        if max_sum >= sum_:
            max_sum = sum_

    for i in range(100):
        sum_ = 0
        sum_ += arr[i][i]

    if max_sum >= sum_:
        max_sum = sum_

    for i in range(100):
        sum_ = 0
        sum_ += arr[i][100 - i - 1]

    if max_sum >= sum_:
        max_sum = sum_

    print(f'#{tc} {max_sum}')