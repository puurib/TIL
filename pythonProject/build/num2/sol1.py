import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split()))for _ in range(N)]

    r = [0, 0, -1, 1]
    c = [1, -1, 0, 0]
    num_l = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                pass
            else:
                num_l.append([matrix[i][j], i, j])
    num_l.sort()
    walk = [0, 0]
    walk_cnt = 0
    monster= [0, 0]
    customer = [0, 0]
    walk_cnt_lst = []
    cnt = 0
    x = 0
    #print(num_l)
    while cnt != len(num_l)//2:
        customer = num_l[x][1:]
        monster = num_l[len(num_l)-x-1][1:]
        walk_cnt += abs(walk[0] - monster[0]) + abs(walk[1] - monster[1])
        walk_cnt_lst.append(walk_cnt)
        walk_cnt += abs(monster[0] - customer[0]) + abs(monster[1] - customer[1])
        walk_cnt_lst.append(walk_cnt)
        walk = customer
        cnt += 1
        x +=1
    print(f'#{tc} {walk_cnt}')