'''
3143. 가장 빠른 문자열 타이핑

해결 방식
1.
어려웠던 점
1. x

[input.txt]
2
banana bana
asakusa sa
'''

import sys
sys.stdin = open('input.txt')

T = int(input()) # 2개
for tc in range(1, T + 1):
    str1, str2 = input().split()

    # print(f'#{tc} {str1} {str2}')
