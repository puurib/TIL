# 연습 문제 1- 2차원 배열의 절대값 총합
'''
#1 2430
#2 2244
#3 0
'''
# 1. 5x5 배열 초기화 (랜덤 x)
# 2. 각 요소에 대해, 그 요소과 이웃한 요소의 차를 구함 (상 하 좌 우 )
# 3. 절대값을 더함
# 4. 25개의 총합 출력
import sys
sys.stdin = open('input.txt')

T = int(input()) # tc 개수

# 1. 5x5 배열 초기화 (랜덤 x)
for tc in range(1, T+1):
    N = int(input())  # N x N 배열
    matrix = []
    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    # pprint(matrix)

    # 2. 각 요소에 대해, 그 요소과 이웃한 요소의 차를 구함 (상 하 좌 우 )
    rlt = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]
            for d in range(4):
                each_row = r + d_row[d]
                each_col = c + d_col[d]
                # 범위 체크
                if each_row < 0 or each_row > 4 or each_col < 0 or each_col > 4:
                    continue
                else:
                    sub = matrix[r][c] - matrix[each_row][each_col]
                    if sub <= 0:
                        sub = sub * -1

                    rlt += sub
    # 3. 절대값을 더함
    # 4. 25개의 총합 출력
    print(f'#{tc} {rlt}')