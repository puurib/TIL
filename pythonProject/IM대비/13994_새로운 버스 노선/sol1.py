'''
1221_GNS dat문제
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 1001 # 얘주의
    for _ in range(N): #노선수만큼 반복
        K, A, B = map(int, input().split())

        if K ==1: # 일반, 모든 정류장 정차
            for i in range(A, B+1):
                cnt[i] += 1
        
        # B 빼먹지 말기
        elif K ==2: # 급행, A가 짝수면 짝수만, 홀수면 홀수만, B에도 정차
            for i in range(A, B, 2):
                cnt[i] +=1
            cnt[B] += 1

        else: # 광역은 A, B는 별도로 처리
            cnt[A] += 1
            cnt[B] += 1
            for i in range(A + 1, B):
                if A%2 == 1 and i%3== 0 and i%10 != 0: # 홀수, 3의 배수 and 10의 배수가 아닌 경우
                     cnt[i]+= 1
                elif A%2 == 0 and i % 4 == 0:
                    cnt[i] +=1

    maxV = 0

    for i in range(1, 1001): # 얘주의
        if maxV < cnt[i]:
            maxV = cnt[i]

    print(f'#{tc} {maxV}')



