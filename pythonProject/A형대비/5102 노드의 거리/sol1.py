'''
5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 D2
bfs는 최단거리, 큐
'''
import sys
sys.stdin = open('input.txt')


def bfs(v):
    Q = []
    Q.append(v)

    # 방문했어요 표시
    visited[v] = 1

    while Q:
        w = Q.pop(0) # 다음 나오세요

        for i in range(V+1): # 노드의 개수 만큼 반복
            # 연결되어있고 아직 방문하지 않은 것을 큐에 넣어야함
            if field[w][i] == 1 and visited[i] ==0:
                # 연결된 다음 번호 큐에 넣기
                Q.append(i) #w로 착각하면 안됨 

                # 이전 방문 정보에 +1 == 이동한 거리
                visited[i] = visited[w] +1

    # 1번 방법 : return visited[G]
    
    ''' 
    어려우니깐 ..제거 원래는 return visited[G]-1을해야함
    '''

    # while을 다 돌면 그래프를 다 돌음
    if visited[G]: # 골에 방문했다면?
        return visited[G] -1
    else: # 시작한 곳으로부터 다돌았는데 visited[G]이 0이라면 (도착x)
        return visited[G] # 이러면 return 0 이랑 같음



T = int(input())
for tc in range(1, T + 1):

    V, E = map(int, input().split())
    #
    line = [ list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    # 방문 정보
    visited = [0] * (V+1) # 시작번호가 1이라서


    # 0으로 초기화 된 인접 행렬
    field = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    
    # 연결된 곳 1로 만들기
    for each in line:
        start = each[0]
        end = each[1]

        field[start][end] = 1
        field[end][start] = 1

    rlt = bfs(S)

    print(f'#{tc} {rlt}')