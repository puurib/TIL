'''
케이크자르기 - 전치행렬 문제
1. 총 딸기 개수 구하기
2. 각 행을 순회하면서 개별개수의 합 * 2 = 총 딸기개수가 되는 순간이 있으면 반반 나눠지는거임
3. 세로도 구하고
4. 둘다 맞으면 1출력 아니면 0출력
'''

from pprint import pprint

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        total += sum(arr[i])  # 전체 딸기 개수를 구함


    # 가로 - 반이 되면 멈춤
    is_half1 = 0
    rlt1 = ''
    for i in range(N):
        is_half1 += sum(arr[i])

        if is_half1 * 2 == total:
            rlt1 = 'y'
            break
        else:
            rlt1 = 'n'
            

    # 세로 - 반이 되면 멈춤
    arr2 = list(map(list, zip(*arr)))
    is_half2 = 0
    rlt2 = ''
    for i in range(N):
        is_half2 += sum(arr[i])

        if is_half2 * 2 == total:
            rlt2 = 'y'
            break
        else:
            rlt2 = 'n'

    # 가로 세로 둘다 yes라면
    ans = 0
    if rlt1 == 'y' and rlt2 == 'y':
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
    #pprint(arr)