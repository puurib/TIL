'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
두 개 씩 보면 됨
'''
V = int(input())
edges = list(map(int, input().split()))

tree = [[0 for _ in range(3)] for _ in range(V+1)]
'''
[
    왼쪽 자식 / 오른쪽 자식 / 부모순으로 저장
    [0,0,0],
    [0,0,0],
    ...
]
'''

# 1. 전위 순회 (preorder)
def preorder(node):
    '''
    전위 순회를 하는 함수입니다.
    # (root를 기준으로) root -> 왼쪽 자식 -> 오른쪽 자식
    # root -> 왼쪽 서브트리의 root -> 오른쪽 서브트리의 root
    :param node: 노드의 번호이자, 현재 방문하는 노드입니다.
    :return: 없습니다.
    '''
    # 자식이 없으면 무한 루프가 걸릴 수 있어서, 자식있을때만 돌기
    if node: 
        # 1. root 방문
        print(node)
        # 2. 왼쪽 방문
        preorder(tree[node][0])
        # 3. 오른쪽 방문
        preorder(tree[node][1])

# 2. 중위 순회 (inorder)
def inorder(node):
    '''
    중위 순회를 하는 함수입니다.
    # (root를 기준으로) 왼쪽 자식 -> root -> 오른쪽 자식
    # 왼쪽 서브트리의 root -> root -> 오른쪽 서브트리의 root
    :param node: 노드의 번호이자, 현재 방문하는 노드입니다.
    :return: 없습니다.
    '''
    # 자식이 없으면 무한 루프가 걸릴 수 있어서, 자식있을때만 돌기
    if node:
        # 2. 왼쪽 방문
        inorder(tree[node][0])
        # 1. root 방문
        print(node)
        # 3. 오른쪽 방문
        inorder(tree[node][1])

# 2. 후위 순회 (postorder)
def postorder(node):
    '''
    후위 순회를 하는 함수입니다.
    # (root를 기준으로) 왼쪽 자식 -> 오른쪽 자식 -> root
    # 왼쪽 서브트리의 root -> 오른쪽 서브트리의 root -> root
    :param node: 노드의 번호이자, 현재 방문하는 노드입니다.
    :return: 없습니다.
    '''
    # 자식이 없으면 무한 루프가 걸릴 수 있어서, 자식있을때만 돌기
    if node:
        # 2. 왼쪽 방문
        postorder(tree[node][0])
        # 3. 오른쪽 방문
        postorder(tree[node][1])
        # 1. root 방문
        print(node)


# 2칸씩 볼 것
for i in range(0, len(edges)-1, 2):
    parent_node = edges[i] # 부모 노드 (현재 노드)
    child_node = edges[i+1] # 자식 노드
    
    # 만약 왼쪽 자식이 비어있으면 넣고
    if tree[parent_node][0] == 0:
        tree[parent_node][0] = child_node
    # 그렇지 않으면 오른쪽 자식에 삽입
    else:
        tree[parent_node][1] = child_node

    # 자식 노드의 부모 설정
    tree[child_node][2] = parent_node

# tree 출력
for i in range(V+1):
    print(tree[i])


# 전위순회
print('----전위 순회----')
start_node= 1
preorder(start_node)
print('----전위 순회 끝----')

# 중위순회
print('----중위 순회----')
start_node= 1
inorder(start_node)
print('----중위 순회 끝----')

# 후위순회
print('----후위 순회----')
start_node= 1
postorder(start_node)
print('----후위 순회 끝----')