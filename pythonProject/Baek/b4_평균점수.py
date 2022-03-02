n_sum = 0
for _ in range(5):
    n = int(input())
    if n < 40:
        n_sum += 40
    else:
        n_sum += n

rlt = int(n_sum / 5)

print(rlt)