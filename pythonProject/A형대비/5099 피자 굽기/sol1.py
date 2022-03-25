'''
5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 D3
O(N)
'''
import sys
sys.stdin = open('input.txt')

def pizza(N, M, arr):
    # 화덕 준비
    Q = []
    # 화덕의 크기만큼 피자를 채워요 (N개 만큼 채울 수 있음)
    for i in range(1, N+1):
        Q.append(i)
        # 여기까지 하면 피자 번호가 Q에 들어가 있음

    idx = N+1 # 이 다음에 들어갈 피자 번호
    
    top = 0 # 피자 번호가 저장될 곳

    # 리스트안에 원소가 있는 동안 while이 돌음
    # 화덕에 피자가 있는 동안 반복
    while Q: 
        # 화덕에서 가장 앞에 있는 피자 번호를 꺼내요 (가장 앞= 화덕 입구에 있는피자)
        top = Q.pop(0)

        # 1. 지금 꺼낸 피자에 치즈가 남았으면
        if arr[top] //2 !=0 :
            # 치즈 녹여요
            arr[top] //= 2
            # 여기주의!!! 다시 화덕의 맨 뒤에 넣어요.
            Q.append(top)

        # 2. 더 들어갈 피자가 있으면
        elif idx <= M:
            # 이거 화덕에 넣자
            Q.append(idx)
            # 다음 피자 준비
            idx += 1

    return top



T = int(input())
for tc in range(1, T + 1):
    # N: 화덕의 크기, M: 피자 개수
    # N < M일 때가 있을 수 있음
    N, M = map(int, input().split())

    # 깔끔하게 짜려고 0 넣어줌
    arr = [0] + list(map(int, input().split()))

    rlt = pizza(N, M, arr)

    print(f'#{tc} {rlt}')