'''
5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

N이 주어졌을 때,
완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과
N/2번 노드(N이 홀수 인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
# 중위탐색
def inorder(node):
    global number
    if 1 <= node <= N:
        # 왼쪽
        left_node = node * 2
        if 0 < left_node < N + 1:
            inorder(left_node)

        tree[node] = number
        number += 1

        # 오른쪽
        right_node = node * 2 + 1
        if 0 < right_node < N + 1:
            inorder(right_node)



for tc in range(1, T + 1):
    # N: 노드의 개수
    N = int(input())
    # tree 배열
    tree = [0] * (N + 1)
    number = 1
    inorder(1)
    print(f"#{tc}", tree[1], tree[N // 2])