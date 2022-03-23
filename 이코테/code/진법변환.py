num = 149
lst = []


while num >= 1:
    lst.append(num % 2)
    num = num //2

rlt = lst[::-1]
for i in rlt:
    print(i, end='')




