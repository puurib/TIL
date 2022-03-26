'''
bj1260 DFS, BFS
'''
# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())

# 빈 리스트를 n+ 1개 만듦 --> 더 간편함
# graph = [[], [], [], [], []]
graph = [[] for _ in range(N+1)]
print(graph)
for _ in range(M):
    # i출발, j도착
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for row in graph:
    print(row)