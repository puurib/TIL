'''
5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

# 전위 순회 함수
def preorder(node):
    # 순회할 때 마다 count 추가.
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

# 테스트 케이스 입력
for tc in range(1, T + 1):
    # 노드 갯수 count 하기 위한 변수 선언
    cnt = 0
    e, n = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(e+2)]

    # 트리 리스트 구조 잡기
    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]
        child_node = edges[i+1]

        if tree[parent_node][0] == 0:
            tree[parent_node][0] = child_node
        else:
            tree[parent_node][1] = child_node

        tree[child_node][2] = parent_node

    preorder(n)

    print(f'#{tc} {cnt}')