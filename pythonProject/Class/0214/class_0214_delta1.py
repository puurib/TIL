from pprint import pprint

num_list = [[1,2,3],[4,5,6],[7,8,9]]

for r in range(len(num_list)):
    for c in range(len(num_list[0])):
        # 지금 값이 5라면 상하좌우 출력하는 값 짜기
        if num_list[r][c] == 5:
            print(num_list[r - 1][c], end=" ") # 상
            print(num_list[r + 1][c], end=" ") # 하
            print(num_list[r][c - 1], end=" ") # 좌
            print(num_list[r][c + 1], end=" ") # 우
