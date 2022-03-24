'''
1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 D3
'''
import sys, math
sys.stdin = open('input.txt')
patterns =  {
    (3,2,1,1) : 0,
    (2,2,2,1) : 1,
    (2,1,2,2) : 2,
    (1,4,1,1) : 3,
    (1,1,3,2) : 4,
    (1,2,3,1) : 5,
    (1,1,1,4) : 6,
    (1,3,1,2) : 7,
    (1,2,1,3) : 8,
    (3,1,1,2) : 9,
    }

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input()))for _ in range(N)]

    '''for row in data:
        print(data)'''

    # 패턴 비율로 암호 숫자를 찾기
    # 각 행의 맨 뒤에서부터 1찾기 : 1을 찾으면 패턴의 시작을 찾은 것임.
    for i in range(N):
        idx = M-1
        password = []
        # 55번 인덱스까지만 확인하면됨, 55번이 1이 아니면, 암호코드가 될 수 없음.
        while idx >= 55:
            if data[i][idx] == 1: # 패턴 시작
                for _ in range(8):
                    c1 = c2 = c3 = c4 = 0 # 패턴의 각 부분의 길이

                    # 0101순서로 됨
                    # 1의 개수 c4에 저장
                    while data[i][idx] ==1:
                        c4+= 1
                        idx -=1
                    # 0의 개수 c3에 저장
                    while data[i][idx] ==0:
                        c3+= 1
                        idx -=1
                    # 1의 개수 c2에 저장
                    while data[i][idx] ==1:
                        c2+= 1
                        idx -=1
                    # 0의 개수 c1에 저장 (총길이가 7개이기 때문에 3개를 알면 자동으로 알수 있음)
                    c1= 7- c2- c3- c4
                    # idx -= c1
                    password.insert(0, patterns[(c1, c2, c3, c4)])
                else:
                    idx -= 1 #

    print(f'{tc}')








