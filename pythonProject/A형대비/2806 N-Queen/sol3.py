'''
2806. N-Queen D3 교수님 풀이
'''
import sys, math
from pprint import pprint
sys.stdin = open('input.txt')
def promising(v):
    # 세로
    for i in range(v):
        if row[v] == row[i] or abs(row[v] - row[i])== v-i:   # 유망하지 않은 것 , 앞에 나와 같은 값이 있는 것 / abs(컬럼의 차)
            return False
    
    # for문을 다 돌았는데 False가 안나왔다면
    return True

def dfs(v):
    global cnt
    # [1] 탈출 조건 : 행번호가 N이 된 경우 = 성공
    if v == len(row):                # len(row) == N
        cnt += 1
        return
    else:                            # v가 종료조건인 마지막 줄이 아니면
        for i in range(len(row)):
            row[v]= i  # v번째 row에 i컬럼에 퀸을 두겠다.
            if promising(v):   # check : 그냥 다음줄로 가는게 아니라 체크하기 - promising이 가지치기
                dfs(v+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 체스판 크기 N
    row = [0]*N        # ???? visit - 2차원으로 해도 되는데 1차원으로 해도 되니깐
    cnt = 0          # 결과
    dfs(0)

    print(f'#{tc} {cnt}')
