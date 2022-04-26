# Python 으로 JS 따라하기

def add(a, b):
    rlt = a+b
    return rlt

def mul(a, b):
    rlt = a*b
    return rlt


calculator =  {
    'add': add,
    'mul': mul
}
rlt_1 = calculator['add'](1, 2)
rlt_2 = calculator['mul'](3, 4)

print(rlt_1) # 3
print(rlt_2) # 12