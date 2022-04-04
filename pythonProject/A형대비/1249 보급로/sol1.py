'''
1249. [S/W 문제해결 응용] 4일차 - 보급로 D4 (라이브러리 사용X)
중복방문 BFS 조건에 따라 갱신
특정 위치나 시간 경로를 찾아갈 때 사용 가능
'''
import sys, math
from pprint import pprint
sys.stdin = open('input.txt')

def BFS(si, sj, ei, ej): #시작 끝점
    q = [] # [1] q, v 생성
    v = [[100000] * N for _ in range(N)]

    q. append((si, sj))  # [2] q 초기데이터들 삽입, v표시
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        # 네방향/8방향/숫자차이가 일정값이하..
        for di, dj in ((-1, 0), (1, 0), (0, -1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0<= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
    return v[ei][ej]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = BFS(0, 0, N-1, N-1)
    print(f'#{tc} {ans}')
    #pprint(arr)
