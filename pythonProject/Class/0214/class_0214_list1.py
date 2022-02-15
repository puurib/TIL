# 2차원 리스트 하나씩 출력하기

num_list = [[1,2,3],[4,5,6],[7,8,9]]

for r in range(len(num_list)):
    for c in range(len(num_list[0])):
        print(num_list[r][c], end=" ")