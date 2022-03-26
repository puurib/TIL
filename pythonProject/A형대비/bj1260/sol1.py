'''
bj1260 DFS, BFS
'''
# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
#  M개의 줄에는 간선이 연결하는 두 정점의 번호 리스트 line
#line = [list(map(int, input().split())) for _ in range(M)]

# 연결리스트
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1


for a in matrix:
    print(a)

# BFS 함수


# DFS 함수
