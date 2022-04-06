# 중복을 제거 하고 알파벳 순서대로 출력

lst= ['A', 'B', 'T', 'A', 'A', 'A', 'B', 'A', 'A']

lst = list(set(lst))

lst.sort()
print(lst)