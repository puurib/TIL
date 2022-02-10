# baby-gin
# 0~9 임의의 카드 6장을 뽑았을 때 3장의 카드 연속 - run, 동일한 번호- triplet
'''
9
111456
123123
233677
112233
333333
123456
667767
054060
101123
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [0] * 12 # tc의 값을 저장할 arr를 생성 (0~9까지의 값 저장)
    for i in range(6):
        arr[n % 10] += 1
        n //= 10

    j = 0
    tri = run = 0
    while j < 10:
        # triplet 삭제
        if arr[j] >= 3:
            arr[j] -= 3
            tri += 1
            continue
        # run 삭제
        if arr[j] >= 1 and arr[j+1] >= 1 and arr[j+2] >= 1:
            arr[j] -= 1
            arr[j+1] -= 1
            arr[j+2] -= 1
            run += 1
            continue
        j += 1

    if run + tri == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


