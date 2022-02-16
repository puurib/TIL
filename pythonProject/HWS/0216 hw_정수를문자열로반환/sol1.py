'''
정수를 문자열로 반환

해결 방식
1. number, strings 리스트를 각각 만들어 놓고 인덱스로 접근
2. 몫, 나머지를 이용해서 str형식으로 만들고
3. 맨 끝부터 새로 정렬한다.

어려웠던 점
1. 처음에 %와 // 으로 접근하려고 했는데, 그 이상은 모르겠어서 sos를 쳤다.
2. number, strings 리스트를 각각 만들어 놓고 이용하는 방법이 잘 안떠올랐다..
3. 음수는..? abs()를 씀..ㅎ

[input.txt]
5
3
1461
4671224
85761
-1
'''

import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 테스트 케이스
T = 6

# 테스트 케이스 만큼 입력 받기
for test_case in range(1, T + 1):

    def itoa(n):
        n = abs(n)
        number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num_to_str = ''
        while n != 0:
            for i in range(len(number)):
                if n % 10 == number[i]:
                    num_to_str += strings[i]
            n = n // 10

        rlt = num_to_str[::-1]

        return rlt

    num = int(input())

    if num >= 0:
        ans = itoa(num)
    else:
        ans = f'-{itoa(num)}'
    # 출력
    print(f'#{test_case} {ans} {type(ans)}')