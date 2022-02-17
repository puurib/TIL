N = int(input())
numbers = []
for i in range(1, N+1):
    if N % i == 0:
        numbers.append(i)

numbers= numbers[1:len(numbers)-1]

if N != 1:
    for i in numbers:
        print(i)
