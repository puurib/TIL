'''
1232. [S/W 문제해결 기본] 9일차 - 사칙연산
'''
import sys
sys.stdin = open('input.txt')

T = 10
'''
        후위 순회 함수입니다.
        왼쪽 서브트리의 root => 오른쪽 서브트리의 root => root
'''
def postorder(v):
    global arr
    if not v:
        return
    
    postorder(L[v])
    postorder(R[v])
    arr.append(tree[v])

# 계산
def cal(lst):
    stack = []
    while lst:
        val = lst.pop(0)
        if val in symbol:
            a = stack.pop()
            b = stack.pop()
            if val == '+':
                stack.append(b + a)
            elif val == '-':
                stack.append(b - a)
            elif val == '*':
                stack.append(b * a)
            else:
                stack.append(b // a)
        else:
            stack.append(int(val))
    return stack[0]

# 사칙연산
symbol = ['+', '-', '*', '/']
for tc in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    tree = [0] * (N + 1)
    for _ in range(N):
        temp = list(map(str, input().split()))
        i = int(temp[0])
        tree[i] = temp[1]
        if len(temp) >= 3:
            L[i] = int(temp[2])
        if len(temp) == 4:
            R[i] = int(temp[3])
    arr = []
    postorder(1)
    print('#{} {}'.format(tc, cal(arr)))