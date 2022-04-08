'''
1238. [S/W 문제해결 기본] 10일차 - Contact D4
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')


def BFS(s):
    # [2] 큐 초기화, 초기데이터(들) 삽입, 방문표시, sol(정답처리위한)
    q = []
    q.append(s)
    visited[s] = 1
    sol = s    # sol 정답처리 사용 위한 변수

    # [3] q에 노드가 있다면 꺼내고
    while q:
        c = q.pop(0) # c = current

        # [4] 종료조건 처리
        if visited[sol] < visited[c] or (visited[sol]== visited[c] and sol <c) :
            sol = c

        # [5] for문 돌리기
        for j in range(1, 101):
            if adj[c][j] and not visited[j]:
                # [6] 조건에 맞으면 큐에 넣고, 방문표시
                q.append(j)
                visited[j] = visited[c] +1

    return sol



T = 10
for tc in range(1, T + 1):
    # N 노드의 수 S 시작점
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    # [0] 인접행렬, visited 배열 초기화
    adj = [[0] * 101 for _ in range(101)]
    visited = [0] * 101

    # [1] lst 연결값을 인접행렬에 저장
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]] = 1

    ans = BFS(S)
    print(f'#{tc} {ans}')
    #print(lst)