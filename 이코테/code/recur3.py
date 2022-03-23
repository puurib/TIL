def f(i, N, v):
    if v == A[i]:
        return 1
    else:
        f(i+1, N, v)
    return -1

A = [7, 2, 5, 4, 1, 3]
N = len(A)
v = 5

print(f(0, N, v))
