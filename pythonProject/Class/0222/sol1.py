'''
2
()()((()))
((()((((()()((()())((())))))
을 입력받으면 True, False 가 리턴되어야함

'''

from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):


    def stack(lst):
        lst = input()
        open = 0
        close = 0
        new_lst = []
        i = new
        while i != 0:
            if lst[0] == ')':
                return False

            if lst[i] == '(':
                open += 1
                new_lst.append(lst[i])
            elif lst[i] == ')':
                close += 1
                new_lst.append(lst[i])

            if ')' in new_lst:
                new_lst[:(i-2)]


        return True
    rlt = stack()
    print(f'#{tc} {rlt}')