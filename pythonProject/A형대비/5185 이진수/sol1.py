'''
5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
[input.txt]
3
4 47FE
5 79E12
8 41DA16CD
'''
import sys, math

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()
    M_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    rlt = ''
    num = 0
    for i in range(len(M)-1,-1,-1):
        # 숫자 변환 
        if M[i] in M_dict:               # M_dict에 없으면 오류
            num = M_dict[M[i]]

        for _ in range(4):
            rlt = str(num%2) +rlt
            num //= 2

    print(f'#{tc} {rlt}')