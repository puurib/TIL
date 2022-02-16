'''
SWEA 1213 GNS

해결 방식
1. DAT(Date Address Table)를 사용해서, dat 빈 배열을 생성해주고
2. 입력받은 배열과 arr가 같으면 dat 인덱스에 1을 더해줌
3. arr와 동일한 dat 인덱스 값을 곱해서 출력해줌

어려웠던 점
1. 마지막에 arr[i] * dat[i] 는 문자 * 숫자여서 ZROZRO이렇게 붙어서 나왔는데 공백을 어떻게 더해줘야할지, 몰랐었다. 중간에 넣어주려고 join()을 사용하려고 했는데 그게 아니라,
(문자 + ''(빈 문자) ) * 숫자로 , 출력형식을 지킴.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(str, input().split())
    k = int(K)
    input_arr = list(map(str, input().split()))
    arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dat = [0] * 10

    for idx in input_arr:
        for i in range(len(arr)):
            if idx == arr[i]:
                #print(arr[i])
                dat[i] += 1

    rlt = ''
    for i in range(len(arr)):
        rlt += (arr[i]+' ') * dat[i]

    print(f'#{tc} {rlt}')