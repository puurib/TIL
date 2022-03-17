'''
5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진힙

1000000이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고,
마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성하시오.

heap : 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 or 가장 작은 노드를 찾기 위해 만들어진 자료구조

# 삽입 연산

1) 최대 힙일때
삽입할 자리 확장 후 확장한 자리에 삽입할 원소 저장
if tree[child] > tree[parent]: # 삽입한 자리의 노드와 부모 노드 간 키 값을 비교합니다.
tree[child], tree[parent] = tree[parent], tree[child] #부모 노드와 자식 노드의 키 값을 교환합니다.
부모 노드가 존재하는 경우 비교 과정을 다시 수행합니다.

else:
삽입 과정을 종료합니다.

2) 최소 힙일때,
삽입할 자리 확장 후 확장한 자리에 삽입할 원소(노드)를 저장

if tree[child_idx] < tree[parent_idx]: # 삽입한 자리의 노드와 부모 노드 간 키 값을 비교합니다.
tree[child_idx], tree[parent_idx] = tree[parent_idx], tree[child_idx] # 부모 노드와 자식 노드의 키 값을 교환합니다.
부모 노드가 존재하는 경우 비교 과정을 다시 수행합니다.

else:
삽입 과정을 종료합니다.
'''


import sys
sys.stdin = open('input.txt')

T = int(input())
# 중위탐색

def change_value(child_idx):
    parent_idx = parent_list[child_idx]

    # 루트 노드인 경우
    if parent_idx == 0:
        return

    parent_value = tree[parent_idx]
    child_value = tree[child_idx]

    if parent_value > child_value:
        tree[parent_idx], tree[child_idx] = tree[child_idx], tree[parent_idx]
        change_value(parent_idx)


def sum_parent_value(child_idx):
    global result
    # 부모 노드 인덱스 구하기
    parent_idx = parent_list[child_idx]
    # 부모 노드가 없다면, 종료
    if parent_idx == 0:
        return

    # 부모 노드가 있다면, 값을 더하기
    result += tree[parent_idx]
    # 부모 노드 탐색
    sum_parent_value(parent_idx)


for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    # 입력한 값을 담을 tree 배열
    tree = [0] * (N + 1)
    # 부모 리스트 추가
    parent_list = [0] * (N + 1)
    for i in range(1, N + 1):
        # 자식 인덱스에 부모 인덱스를 값으로 넣음
        parent_list[i] = i // 2
        # 노드 인덱스(루트 노드가 1로 시작하는)에 해당하는 키 값을 저장
        tree[i] = data[i - 1]

    # 조건에 맞춰 노드 정렬
    for i in range(1, N + 1):
        change_value(i)

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    result = 0
    sum_parent_value(N)
    print(f"#{tc} {result}")