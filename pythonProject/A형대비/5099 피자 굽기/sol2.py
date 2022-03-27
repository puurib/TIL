import sys
sys.stdin = open('input.txt')

def pizza(N, M, arr):
    q = []
    for i in range(1, N+1):
        q.append(i) # 피자 번호 넣기

    idx = N + 1
    top = 0 # 피자번호 저장될 곳

    while q:
        top = q.pop(0)
        if arr[top] // 2 != 0:
            arr[top] //= 2
            q.append(top)

        elif idx <= M:
            q.append(idx)
            idx+=1

    return top

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 일부러 0 붙어서 인덱스 맞추기
    arr = [0] + list(map(int, input().split()))

    rlt = pizza(N, M, arr)
    print(f'#{tc} {rlt}')