'''
2806. N-Queen D3 룩업테이블 사용
'''
import sys, math
from pprint import pprint
sys.stdin = open('input.txt')

# check 함수가 사라짐

def DFS_1(n):
    global ans
    # 행번호가 N이 된 경우 = 성공
    if n== N:
        ans += 1
        return

    # DFS_1은 이부분이 바뀜
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j]= v3[n-j] = 1
            DFS_1(n+1)
            v1[j] = v2[n+j]= v3[n-j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
    # N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
    v1, v2, v3 = [0]*30, [0]*30, [0]*30
    ans = 0
    # DFS는 꼭대기부터
    DFS_1(0)

    print(f'#{tc} {ans}')
