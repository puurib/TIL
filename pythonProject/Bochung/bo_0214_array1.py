arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
y, x = map(int, input().split()) # 1 1 엔터
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

ans = 0

for i in range(4): # i = 0 기준점으로 부터 위
    dy = directy[i] + y
    dx = directx[i] + x
    ans += arr[dy][dx]

    #if dy < 0 or dx < 0 or dy > 2 or dx > 2: continue

    if 0 <= dy < 3 and 0 <= dx < 3: # 배열 범위 안에 있다면
        ans += arr[dy][dx]
print(ans)