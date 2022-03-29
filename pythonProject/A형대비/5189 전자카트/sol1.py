'''
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
'''
from pprint import pprint
import sys, math
sys.stdin = open('input.txt')

def search(cnt, x, total):
    global rlt

    # N이면 마지막 사무실에 들어와야함
    if cnt == N:
        total += arr[x][0]
        # total이 더 작으면 갱신
        if total < rlt:
            rlt = total
            return

    # 시간초과될 수 있으니
    if total > rlt:
        return

    # 돌기
    for i in range(1, N):
        if not arr[x][i]:
            continue
        if not visited[i]:
            visited[i] = 1
            search(cnt+1, i, total+arr[x][i])
            visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited 방문표시 일차원리스트로 충분
    visited = [0 for _ in range(N)]

    # rlt
    rlt = 100 * N
    # 1회차부터 시작
    search(1, 0, 0)
    print(f'#{tc} {rlt}')
