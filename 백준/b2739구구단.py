# N = int(input())

# for i in range(1, 10):
#     rlt = N * i
#     print(f'{N} * {i} = {rlt}')

# 함수화
def gugudan(N):
    n_dan = ''
    for i in range(1, 10):
        rlt = N * i
        n_dan = '{N} * {i} = {rlt}'

N = int(input())
gugudan(N)
