# IM LED 조명 정답 예시 코드
import sys
from pprint import pprint
sys.stdin = open('input.txt')
T=int(input())
for t in range(1,T+1):
    N=int(input())
    LED=list(map(int,input().split()))
    LED=[0]+LED

    def operate(n):
        for i in range(n,len(LED)):
            if i%n==0:
                if LED[i]==1:
                    LED[i]=0
                elif LED[i]==0:
                    LED[i]=1

    cnt=0
    while sum(LED):
        for i in range(1,len(LED)):
            if LED[i]==1:
                operate(i)
                cnt+=1

    print(f'#{t} {cnt}')