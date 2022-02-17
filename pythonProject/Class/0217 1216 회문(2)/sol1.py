'''
1216. [S/W 문제해결 기본] 3일차 - 회문2

해결 방식
1. 간단하게 if str1 in str2
이렇게 in 연산자를 이용해 문자열에 이 값이 있는가? 로 비교했다.

어려웠던 점
1. x

[input.txt]
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''

import sys, pprint
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    str1 = []
    for row in range(100):
        str1.append((input()))
    print(f'{tc}')
    pprint.pprint(f'{str1}')
