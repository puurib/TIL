# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = list(zip(*a))
# print(b)
m = 10
a = 'JAEZNNZEAJ'
i = 0
while i != int(m/2):
    if a[i] == a[-i-1]:
        rlt = 1
    else:
        rlt = 0
        break
    i += 1

print(rlt)



