A, B = map(int, input().split())
rlt =''
if A > B:
    rlt = 'Yes'
elif A == 0 and B == 0:
    pass
elif A <= B:
    rlt = 'No'

print(rlt)