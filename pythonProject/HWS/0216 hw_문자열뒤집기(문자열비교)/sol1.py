'''
문자열 뒤집기(문자열 비교)

해결 방식
1. 슬라이싱으로 해결

어려웠던 점
1. x

'''

import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 테스트 케이스
T = int(input())

# 테스트 케이스 만큼 입력 받기
for test_case in range(1, T + 1):


    def slicing(word):
        reverse_word = word[::-1]
        return reverse_word

    # 출력
    w = input()

    print(f'#{test_case} {slicing(w)}')