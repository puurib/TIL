import sys
sys.stdin = open('input.txt')

T = int(input())
# 0. T = tc의 개수, N = 첫 줄에 양수의 개수  numbers = N개의 양수
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # arr 내에서 min_val max_val을 찾을 거야.
    min_val = arr[0]
    max_val = arr[0]
    for i in range(N): # N이 5라면 범위는 0~4 (! 범위는 항상 주의하자)
        if min_val >= arr[i]:
            min_val = arr[i]

        if max_val <= arr[i]:
            max_val = arr[i]


    rlt = max_val - min_val

    print(f'#{tc} {rlt}')