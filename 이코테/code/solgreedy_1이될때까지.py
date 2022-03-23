N = 25
K = 5
cnt = 0

while N > 1:
    if N % K != 0:
        N = N - 1
    else:
        N = N // K

    cnt += 1

print(cnt)
