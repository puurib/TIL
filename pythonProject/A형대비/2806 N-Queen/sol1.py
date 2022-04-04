'''
2806. N-Queen D3
'''
import sys, math
from pprint import pprint
sys.stdin = open('input.txt')

def check(si, sj):
    # [1]위쪽 방향
    for i in range(si-1, -1, -1):
        if v[i][sj] == 1:
            return 0

    # [2] 좌측 대각선 위
    i, j = si-1, sj -1
    while i >= 0 and j >=0:
        if v[i][j] == 1:
            return 0
        i, j = i-1, j-1

    # [3] 우측 대각선 위
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if v[i][j] == 1:
            return 0
        i, j = i - 1, j + 1

    # 3방향 퀸 없음 : 성공
    return 1

def DFS(n):
    global ans
    # 행번호가 N이 된 경우 = 성공
    if n== N:
        ans += 1
        return

    for j in range(N):
        if check(n, j):
            v[n][j]= 1
            DFS(n+1)
            v[n][j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
    # N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
    v = [[0]*N for _ in range(N)]
    ans = 0
    # DFS는 꼭대기부터
    DFS(0)

    print(f'#{tc} {ans}')
