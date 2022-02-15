# 1. matrix 초기화
N = int(input())
matrix = []
r = []
for i in range(N):
    for j in range(N):
        #print(num_list[i][j])
        row = []
        row = (N * i) + j + 1
        if j == N-1:
            matrix.append(row)
print(matrix)
# 2. 각각의 요소의 차 구하기
5

