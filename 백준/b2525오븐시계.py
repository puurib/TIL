A, B = map(int, input().split())
C = int(input())
h = 0 # 시간
m = 0 # 분
if B + C >= 60:
    h = A + ((B + C) // 60)
    m = (B + C) % 60
    if h > 23:
        h = A + ((B + C) // 60) - 24
        
    print(f'{h} {m}')
else:
    h = A
    m = B + C 
    print(f'{h} {m}')