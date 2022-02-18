'''
1859. 백만 장자 프로젝트

해결 방식
1.

어려웠던 점
1.

'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input()) # tc수 = 1

for tc in range(1, T + 1):
    N, Q = map(int, input().split())

    # 이렇게 상자 추가 해주는 부분.. 앞뒤로 추가해주면 좀 더 편하게 풀 수 있는 트릭.
    arr = [0] * (N+1)


    for i in range(1, Q+1): # 범위 잘보기
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i


    # 출력하는 것도 연습해야겠다. (언팩 연산자를 이용해서 출력하는 거 유의하기)
    print(f'#{tc}', *arr[1:])








