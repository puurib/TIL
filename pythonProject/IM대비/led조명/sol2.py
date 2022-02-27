# IM LED 조명 정답 예시 코드
import sys
from pprint import pprint
sys.stdin = open('input.txt')

TC = int(input())

for test_case in range(1, TC + 1):
    length_N = int(input())
    led = [0] * (length_N + 1)
    led_rlt = list(map(int, input().split()))
    print(led_rlt)
    led_rlt.insert(0, 0)
    print(led_rlt)
    count = 0

    # solve
    for i in range(length_N + 1):
        if i == 0: # 0은 안함
            continue
        if led[i] == led_rlt[i]:  # led_rlt[i]가 0이면 안함
            continue
        else:  # press button
            for j in range(i, length_N + 1):
                if j % i == 0:  # change
                    if led[j]:
                        led[j] = 0
                    else:
                        led[j] = 1
            count += 1

        if led == led_rlt:
            print(f"#{test_case} {count}")
            break