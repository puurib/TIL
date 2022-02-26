'''
오목판정 (보충)
'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input()) # tc수 = 1

for tc in range(1, T + 1):
    N = int(input()) # N X N 크기의 판

    arr = [list(input()) for _ in range(N)]


    # 가로 세로 대각선을 보면서 o이 있나 없나 판별
    cnt = 0 # 5면 끝남

    # 1. 가로
    rlt1 = ""
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1

        if cnt >= 5:
            rlt1 = "YES"
            break
        else:
            rlt1 = "NO"

    # 2. 세로
    rlt2 = ""
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 'o':
                cnt += 1

        if cnt >= 5:
            rlt2 = "YES"
            break
        else:
            rlt2 = "NO"

    # 3. 대각선
    rlt3 = ""
    cnt = 0
    for i in range(N):
    
        if arr[i][i] == 'o':
            cnt += 1

        if cnt >= 5:
            rlt3 = "YES"
            break
        else:
            rlt3 = "NO"

    # 4. 대각선
    rlt4 = ""
    cnt = 0

    for i in range(N):
        if arr[i][N-i-1] == 'o':
            cnt += 1

        if cnt >= 5:
            rlt4 = "YES"
            break
        else:
            rlt4 = "NO"

    # 값
    if "YES" == rlt1 or "YES" == rlt2 or "YES" == rlt3 or "YES" == rlt4:
        rlt = "YES"
    else:
        rlt = "NO"


    print(f'#{tc} {rlt}')









