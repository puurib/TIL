'''
1865. 동철이의 일 분배 D4
'''
import sys
sys.stdin = open('input.txt')
# w = 몇번째 일꾼, # per = 퍼센트
def search(w, per):
    global rlt
    # 가치지기 해줘야함 : 보통 작고크고 같고 세게 중에 따져서 넣음
    if per <= rlt:
        return
    #if per == rlt:
        # w가 전체 일꾼이 선택되었음
        # w가 전체 일꾼이 선택되지 않았음
    #    return
    # 종료 조건
    if w == N:
        rlt = max(rlt, per)
        return

    # 아직 모든 일꾼이 선택되지 않았을 때
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1 # 뭔가 조작하고
                search(w+1, per * arr[w][i])
                visited[i] = 0 # 복원해서 다음 dfs할 준비
    return

T = int(input())
'''
재귀 dfs
확률로 받아야 가지치기 때 유망성 조사에 유리함
'''

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 확률로 바꿔주기
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] /100

    # visited, rlt
    visited = [0] * N
    rlt = 0
    # 함수만들기
    search(0, 1)
    print(f'#{tc} {rlt*100:6f}')