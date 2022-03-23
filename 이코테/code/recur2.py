def f3():
    print(a[0])


def f2(dic, key):
    dic[key] = 10

a = [1, 2, 3]
f3()                  # 출력 : 1
f2(a, 0)              # 출력 : [10, 2, 3]
f3()                  # 출력 : 10
print(a)