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
    word = [] #
    for _ in range(N):
        word.append(list(input()))

    for i in range(N):
        for j in range(N-M+1):
            x = word[i][j:j+M]
            if x == x[::-1]:
                print(f'#{tc} {"".join(x)}')

    # 세로
    word1 = list(map(list, zip(*word)))

    for i in range(N):
        for j in range(N-M+1):
            x = word1[i][j:j+M]
            if x == x[::-1]:
                print(f'#{tc} {"".join(x)}')


    # print(f'#{tc} {N} {M}')
    #print(f'--------------')
    #pprint.pprint(f'{sero_matrix}')