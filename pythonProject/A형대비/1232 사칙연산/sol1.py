'''
1232. [S/W 문제해결 기본] 9일차 - 사칙연산
'''

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for _ in range(M):
        leaf, value = map(int, input().split())
        tree[leaf] = value

    for i in range(N, 0, -1):
        tree[i // 2] += tree[i]

    print(f'#{test_case} {tree[L]}')