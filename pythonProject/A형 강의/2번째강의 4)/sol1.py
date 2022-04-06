# 재귀호출

# 순서 10, 9, 8, 7, 6, 6, 7, 8, 9, 10

def num(n):
    if n == 5:
        return
    print(n, end=' ')
    num(n-1)
    print(n, end=' ')

num(10)
