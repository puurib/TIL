import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    cnt = [0] * n
    max_num = 0
    # 최대값 찾아내기.
    for i in range(n-1):
        for j in range(i+1, n):
            if  lst[i] > lst[j]:
                cnt[i] += 1

    # 최대값보다 작은 수 세기
    max_num = cnt[0]
    for i in cnt:
        if max_num <= cnt[i]:
            max_num = cnt[i]


    print(f'#{tc} {max_num}')