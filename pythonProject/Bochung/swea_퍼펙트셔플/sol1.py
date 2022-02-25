'''
퍼펙트 셔플

해결 방식
1.

어려웠던 점
1.

[input.txt]
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    input_arr = list(map(str, input().split()))

    # 반으로 나눈다
    # (N이 홀수일때 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가)
    if N % 2 == 0:
        first_arr = input_arr[0:int(N/2)]
        second_arr = input_arr[int(N/2):]
    else:
        first_arr = input_arr[0:int(N/2)+1]
        second_arr = input_arr[int(N/2)+1:]

    rlt = []
    for n in range(int(N/2)):
        f = first_arr[n]
        s = second_arr[n]
        rlt.append(f)
        rlt.append(s)

    if N % 2 == 1:
        rlt.append(first_arr[-1])

    print(f'#{tc}', end=' ')
    print(*rlt)
