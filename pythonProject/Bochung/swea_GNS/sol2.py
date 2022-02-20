import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    t, N = input().split()
    n = int(N)
    arr = list(input().split())
    dat = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0] * 10

    # arr을 돌면서 몇개 있는지 확인하기 -> i, j를 사용해서 두개를 표현했음
    for i in range(n):
        for j in range(len(dat)):
            if arr[i] == dat[j]:
                cnt[j] +=1

    lst = []
    for i in range(len(cnt)):
        lst.append((dat[i]+' ') *  cnt[i])

    print(f'#{tc}', end= ' ')
    print(*lst)