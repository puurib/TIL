T = int(input())

C_num = 100
S_num = 100
# 경우의 수는 총 3가지 뿐
for i in range(T):
    C, S = map(int, input().split())   
    if C > S:
        S_num -= C
    elif S > C:
        C_num -= S
    else:
        continue

print(C_num)
print(S_num)

