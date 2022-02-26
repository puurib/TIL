from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input()) # tc수 = 1

for tc in range(1, T + 1):
    # 배열 받아오기
    arr = [list(map(int, input().split())) for _ in range(9)]
    num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 스도쿠 검증 절차 1.가로
    rlt1 = 0
    for i in range(len(arr)):
        cnt = [0] * 9  # 다 1씩 있어야 스도쿠 성립
        for j in range(len(arr[0])):
            if arr[i][j] in num_lst:
                cnt[arr[i][j]-1] += 1

        for idx in cnt: # 각 줄마다 시행
            if idx > 1 or idx < 1:
                rlt1 = 0
                break
            elif idx == 1:
                rlt1 = 1

    # 스도쿠 검증 절차 2. 세로
    rlt2 = 0
    for i in range(len(arr)):
        cnt = [0] * 9  # 다 1씩 있어야 스도쿠 성립
        for j in range(len(arr[0])):
            if arr[j][i] in num_lst:
                cnt[arr[j][i] - 1] += 1

        for idx in cnt:  # 각 줄마다 시행
            if idx > 1 or idx < 1:
                rlt2 = 0
                break
            elif idx == 1:
                rlt2 = 1




    print(f'#{tc} {rlt2}')