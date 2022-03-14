import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N : 낚시터의 개수
    N = int(input())
    # 총 3개 고정) # 출입구 위치, 낚시꾼 수
    A_spot = list(map(int, input().split()))
    B_spot = list(map(int, input().split()))
    C_spot = list(map(int, input().split()))
    # 순서대로 정렬
    num_lst = [A_spot[0], B_spot[0], C_spot[0]]
    new_lst1 = []
    new_lst2 = []
    new_lst3 = []
    for j in [A_spot, B_spot, C_spot]:
        for i in num_lst:
            if min(num_lst) == j[0]:
                new_lst1 = j
            elif max(num_lst) == j[0]:
                new_lst3 = j
            else:
                new_lst2 = j

    max(num_lst)
    # 낚시터
    spot = [0] * 61
    '''
    #1 10 [4, 5] [6, 2] [10, 2]
    #2 10 [8, 5] [9, 1] [10, 2]
    #3 24 [15, 3] [20, 4] [23, 7]
    #4 39 [17, 8] [30, 5] [31, 9]
    #5 60 [57, 12] [31, 19] [38, 16]
        
    '''

    cnt = 0
    i = 0

    if new_lst3[0] == N:  # 끝값인 경우
        while new_lst3[1] > cnt:
            if cnt == 0:  # 최초일 때
                spot[new_lst3[0]] = 1
            else:
                spot[new_lst3[0] - i] = 1 + i
            cnt += 1
            i -= 1

    elif new_lst3[0] != N:  # 끝 값이 아닐 때
        while new_lst3[1] > cnt:
            if cnt == 0 and (new_lst3[0] > new_lst1[1] + new_lst2[1]):  # 최초일 때
                spot[new_lst3[0]] = 1
            elif cnt

            cnt += 1






print(f'#{tc} {new_lst1} {new_lst2} {new_lst3}')

