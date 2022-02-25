'''
4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

해결 방식
1.

어려웠던 점
1.

[input.txt]
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input()) # tc수 = 1

for tc in range(1, T + 1):
    arr = list(input().split())
    stack = []
    decimal_cnt = 0
    ans = 0
    ans_error = ''
    for token in arr:
        if token.isdecimal(): # 유효한 숫자인지 아닌지 판별
            stack.append(int(token))
            decimal_cnt += 1
        else:
            if len(stack) > 1: # 연산자를 만난경우
                #print(stack)
                p2 = stack.pop()
                p1 = stack.pop()

                if token == "+":
                    rlt = p1 + p2
                    stack.append(rlt)

                elif token == "-":
                    rlt = p1 - p2
                    stack.append(rlt)

                elif token == "*":
                    rlt = p1 * p2
                    stack.append(rlt)

                elif token == "/":
                    rlt = p1 / p2
                    stack.append(rlt)
                    if p2 == 0:
                        print(f'#{tc} {ans_error}')

            elif token == ".":
                print(f'#{tc}', end= ' ')
                print(*stack)

            elif token in ["+", "/", "-", "*"] and len(stack)<= 1:
                ans_error = 'error'
                print(f'#{tc} {ans_error}')
                break

            elif arr[0:len(arr)-1] == ".":
                ans_error = 'error'
                print(f'#{tc} {ans_error}')




