'''
1974. 스도쿠 검증

해결 방식
1.

어려웠던 점
1.

'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input()) # tc수 = 1

for tc in range(1, T + 1):
    # 배열 받아옴 9x9 행렬
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 모든 숫자
    dat = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = [0] * 9

    #행 체크
    rlt1 = []
    for i in range(9): # 행마다 체크
        cnt = [0] * 9
        for j in range(9):
            if arr[i][j] in dat:
                idx = arr[i][j]
                cnt[idx-1] += 1

        for k in cnt:
            if k >= 2:
                rlt1.append(0)
                break
            else:
                rlt1.append(1)

    # 열 체크
    for j in range(9): # 열마다 체크
        cnt = [0] * 9
        for i in range(9):
            if arr[i][j] in dat:
                idx = arr[i][j]
                cnt[idx-1] += 1

        for k in cnt:
            if k >= 2:
                rlt1.append(0)
                break
            else:
                rlt1.append(1)

    # 3x3 네모 체크
    for i in range(0,9,3):  # 열마다 체크 9-3+1
        for j in range(0,9,3):
            cnt = [0] * 9
            for ii in range(i, i+3):
                for jj in range(j, j+3):
                    if arr[ii][jj] in dat:
                        idx = arr[ii][jj]
                        cnt[idx-1] += 1

            for k in cnt:
                if k >= 2:
                    rlt1.append(0)
                    break
                else:
                    rlt1.append(1)

    # 모두 1이면 1출력
    ans = 1
    for i in rlt1:
        if i == 0:
            ans = 0
            break
    # else:
    #     ans = 1
    print(f'#{tc} {ans}')








