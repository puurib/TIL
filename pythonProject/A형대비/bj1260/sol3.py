# DFS BFS

import sys
from collections import deque

def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in graph[V]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)

print()
visited = [False for _ in range(N+1)]
bfs(V)