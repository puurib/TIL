# N = int(input())

# for i in range(1, 10):
#     rlt = N * i
#     print(f'{N} * {i} = {rlt}')

# 함수화
def gugudan(N):
    n_dan = tuple() # 튜플은 순서가 있는 것.
    for i in range(1, 10):
        rlt = N * i
        n_dan += f'{N} * {i} = {rlt}'
    return n_dan

N = int(input())
gugudan(N)

