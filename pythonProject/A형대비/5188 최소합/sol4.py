'''
5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 D3
'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')
def road(x, y, total):
    global rlt
    # 가지치기
    if total > rlt:
        return rlt

    # 종료 조건 = 도착했다면
    if x == N-1 and y == N-1:
        total += arr[x][y]
        if total < rlt:
            rlt = total
            return rlt
    # 오른쪽 , 아래쪽 이동
    dx = [0, 1]
    dy = [1, 0]

    for k in range(2):
        # 다음 좌표
        cx = x + dx[k]
        cy = y + dy[k]

        # 범위가 넘어가면
        if x > N-1 or y > N-1:
            continue
        # 방문 안했다면
        if not visited[x][y]:
            visited[x][y] = 1
            road(cx, cy, total + arr[x][y])
            visited[x][y] = 0
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문표시 visited
    visited = [[0] * N for _ in range(N)]
    # 결괏값 rlt
    rlt = 10 * 13 * 13

    # 함수 road(x, y, total)
    road(0, 0, 0)
    print(f'#{tc} {rlt}')