T = int(input())
for tc in (1, T+1):
    lst = list(map(str, input().split()))
    rlt = float(lst[0])

    for i in range(1, len(lst)):
        if lst[i] == '@':
            rlt *= 3

        if lst[i] == '%':
            rlt += 5
        if list[i] == '#':
            rlt -= 7

    print('%0.2f' %(rlt))
