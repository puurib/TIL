'''
6190_정곤이의 단조 증가하는 수
[input.txt]
1
4
2 4 7 10
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())

    arr = list(map(int, input().split()))

    lst = []
    for i in range(N):
        for j in range(N):
            if i != j :
                if arr[i] * arr[j] in lst:
                    continue
                else:
                    lst.append(arr[i] * arr[j])

    num_lst = []
    for num in range(len(lst)):
        str_len = len(str(lst[num]))
        if str_len == 1:
            num_lst.append(lst[num])
        else:
            j = 0
            for j in range(str_len):
                if j+1 <= str_len:
                    if int(str_len[j])  <= int(str_len[j+1]):
                        rlt = 'ok'
                else:
                    rlt = 'no'
                    break
            else:
                if rlt == 'ok':
                    num_lst.append(lst[num])
    print(f'#{tc} {num_lst}')
    #pprint(arr)

