# 리스트를 이용한 다익스트라 구현 -> 개선사항으론 최소힙을 이용 import heapq

# 다익스트라는 방향 무방향 다 쓸 수 있지만
# 지금그래프는 방향성 그래프

def dijkstra(s, V):
    visited = [0] * (V+1)
    visited[s] = 1

    # [1] D 배열 초기화 : 출발하는 곳에서 번호에 해당하는 곳까지의 거리 초기화
    for i in range(V+1):
        D[i] = adj[s][i]

    for _ in range(V):
        minV = INF # 선택된 목적지까지 가는 가중치
        w = 0      # 이번에 선택된 목적지

        # 방문하지 않은 노드 중에서 가장 비용이 적은 노드 선택
        for i in range(V+1):
            # 방문 X and minV보다 작다면
            if not visited[i] and minV > D[i]:
                w = i
                minV = D[i]

        visited[w] = 1 # 방문 표시

        # 인접한 노드를 다 돌면서
        for i in range(V+1):
            if 0< adj[w][i] < INF:   # 선택된 곳에서 w -> 이번에 for 문 돌면서 가는 거 i
                # 출발지에서 i로 바로 가는값, w까지 오고 + w에서 i까지 가는 값
                D[i] = min(D[i], D[w]+adj[w][i])

INF = 987654321
# 버텍스, 엣지
V, E = map(int, input().split())
# 가중치
adj = [[INF] *(V+1) for _ in range(V+1)]

for i in range(V+1):
    adj[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w

D = [0] * (V+1)
# 다익스트라함수(시작, 끝)
dijkstra(0, V)

print(D)