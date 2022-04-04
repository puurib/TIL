from collections import deque

n=int(input()) # 전체 사람 수 
s,e=map(int,input().split()) # 두 사람의 번호
m=int(input()) # 간선 수

graph=[[] for _ in range(n+1)]  # 연결리스트

for _ in range(m):
    u,v=map(int,input().split())  # 부모자식관계
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    q=deque([[start,0]])
    visited=[0]*(n+1)
    visited[start]=1
    
    while q:
        v,d=q.popleft()
        if v==e:
            return d
        for w in graph[v]:
            if not visited[w]:
                visited[w]=1
                q.append([w,d+1])

    return -1

print(bfs(s))