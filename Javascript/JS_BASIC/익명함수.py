# Python 으로 JS 따라하기

calculator =  {
    'add': lambda x, y : x + y, 
    'mul': lambda x, y : x * y, 
}
rlt_1 = calculator['add'](1, 2)
rlt_2 = calculator['mul'](3, 4)

print(rlt_1) # 3
print(rlt_2) # 12