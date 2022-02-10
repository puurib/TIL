numbers= [784386, 279993, 982220, 996285, 614710, 992232, 195265, 359810, 919192, 158175]


result = 0
for i in range(len(numbers)-1):
    for j in range(i):

        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

result = numbers[0] - numbers[-1]
print(f'{result}')

# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175