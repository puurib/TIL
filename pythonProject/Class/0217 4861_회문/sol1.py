'''
4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

해결 방식
1. N을 입력받아서 N*N행을 만들어줬다.
2. 1의 배열에서 길이가 M인 회문을 찾아야한다.

어려웠던 점
1.
'''
import sys, pprint
sys.stdin = open('input.txt')

T = int(input()) #
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # NxN행, M은 회문길이
    garo_matrix = [] #
    for _ in range(N):
        row = list(input())   # 가로 matrix
        garo_matrix.append(row)


    # 회문을 찾아보기
    for i in range(len(garo_matrix)): # 행
        for j in range(len(garo_matrix[0])): # 열
            check = 0
            rlt = []
            n = 0
            while n != int(M/2):
                if garo_matrix[i][j] == garo_matrix[i][-j-1-(M-N)]:
                    check = 1
                else:
                    check = 0
                    break
                n += 1

            if check == 1:
                rlt= ''.join(row)
                print(rlt)



    # 세로 matrix
    sero_matrix = list(zip(*garo_matrix))


    # print(f'#{tc} {N} {M}')
    print(f'--------------')
    #pprint.pprint(f'{sero_matrix}')