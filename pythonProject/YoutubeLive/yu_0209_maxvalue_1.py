# 유튜브 라이브 - 최대값 찾기

T = int(input()) # tc 개수

#
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[1]
    for i in range(len(arr)):
        if maxV < arr[i]:
            maxV = arr[i]

    print(arr)
