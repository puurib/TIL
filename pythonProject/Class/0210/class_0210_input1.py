# n = int(input()) # 정수 한 개 입력 받기
# a, b = map(int, input().split()) # 공백을 두고 정수 2개 입력 받기
# lst_1 = list(map(int, input().split())) # 정수 형태를 일차원 리스트로 입력 받기
# lst_2 = [map(int, input().split())] # lst_2의 첫번째 원소로 map(int, input().split())을 넣는 것
#
# lst_3 = list(map(int, input()))
# print(lst_3)  #1234를 입력받아 [1, 2, 3, 4]로 출력하는 것

# 1 2 3 4
# 5 6 7 8

matrix = [] # 빈 리스트 생성
for idx in range(2):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)