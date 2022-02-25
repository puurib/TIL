import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #첫 줄에 카드 장 수
    ai = list(map(int, input()))
    num_lst = list(range(0, 10))
    cnt = [0] * 10


    for i in range(len(ai)):
        if ai[i] in num_lst:
            cnt[ai[i]] += 1

    max_ai = max(cnt)
    for i in range(len(cnt)):
        if max_ai == cnt[i]:
            max_num = i
    print(max_ai, max_num)