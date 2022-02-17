numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    for j in range(i):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]


print(numbers[1])
