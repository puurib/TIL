'''
1970_쉬운거스름돈 - 예시코드
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T=int(input())

for tc in range(1, T+1):
    money=int(input())
    lst=[0]*8
    while money>=50000:
        money -= 50000
        lst[0] +=1
    while money>=10000:
        money -= 10000
        lst[1] +=1
    while money>=5000:
        money -= 5000
        lst[2] +=1
    while money>=1000:
        money -= 1000
        lst[3] +=1
    while money>=500:
        money -= 500
        lst[4] +=1
    while money>=100:
        money -= 100
        lst[5] +=1
    while money>=50:
        money -= 50
        lst[6] +=1
    while money>=10:
        money -= 10
        lst[7] +=1

    print(f'#{tc}')
    print(*lst)

