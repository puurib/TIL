# 1. matrix 초기화
matrix = []
for i in range(5):
    row = [j + i * 5 for j in range(1, 6)]
    matrix.append(row)
    #print(row)

rlt = 0
# 2. 각 요소에 접근하기
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        d_row = [-1, 1, 0, 0] # 상 하 좌 우
        d_col = [0, 0, -1, 1]
        for d in range(4):
            each_row = r + d_row[d]
            each_col = c + d_col[d]
            # 범위 체크 : 없는 값에 접근할 때 index error가 남
            if each_row < 0 or each_row > 4 or each_col < 0 or each_col > 4:
                continue
            else:
                # print(f'target{matrix[r][c]} --> {matrix[each_row][each_col]}')
                # 3. 각각의 요소의 차 구하기
                sub = matrix[r][c] - matrix[each_row][each_col]
                # 4. 절대값 처리하기
                if sub < 0 :
                    sub = -1 * sub
                # 삼항 연산자 sub = sub if sub >= 0 else -sub

                # 5. 합 누적하기기
                rlt += sub

print(rlt)

