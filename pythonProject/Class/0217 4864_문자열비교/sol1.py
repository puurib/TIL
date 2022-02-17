'''
4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

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

import sys
sys.stdin = open('input.txt')

T = int(input()) # 3개
for tc in range(1, T + 1):
    str1 = input()  # 이 문자열을
    str2 = input()  # 아래 문자열에서 일치하는 값을 찾는 거

    if str1 in str2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
