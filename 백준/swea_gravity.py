# 최대값 갱신할 수 있는가, 작은거 큰거 찾아낼 수 있는가
# for문에서 range 범위 제대로 파악할 수 있는가

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    len_lst = len(lst)
    max_v = 0
    # 최대값 찾기 - 나보다 작으면 1더함!
    for i in range(len_lst):
        cnt = 0
        for j in range(i+1, len_lst):
            if lst[i] > lst[j]:
                cnt += 1
            else:
                continue
        
        if max_v <= cnt:
            max_v = cnt


    # x = lst[i] lst의 인덱스값 
    # A는 0, 8
    

    print(f'#{tc} {max_v}')