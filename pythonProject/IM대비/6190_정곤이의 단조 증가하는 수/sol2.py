import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    lst = []
    # arr의 서로 다른 원소를 곱해서 lst에 추가
    for i in range(N):
        for j in range(N):
            if i != j :
                if arr[i] * arr[j] in lst:
                    pass
                else:
                    lst.append(arr[i] * arr[j])


    str_lst = list(map(str, lst)) # str로 형변환
    num_lst = []

    for i in range(len(str_lst)):
        if len(str_lst[i]) == 1:
            pass
        else:
            rlt = ''
            for l in range(len(str_lst[i])-1): #각 원소별로 비교
                if str_lst[i][l] <= str_lst[i][l+1]:
                    rlt = 'y'
                else:
                    rlt = 'n'
                    break

            if rlt == 'y':
                num_lst.append(int(str_lst[i]))

    # 최대값 구하기
    if num_lst:
        max_num = max(num_lst)
    else:
        max_num = -1
    print(f'#{tc} {max_num}')