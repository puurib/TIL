arr = [["A","B","C"],["A","G","H"],["H","I","J"],["K","A","B"],["A","B","C"]]
new_arr = []
for i in range(len(arr)): # 행
    for j in range(len(arr[0])): # 열
        new_arr.append(arr[i][j])
# print(new_arr)

for i in range(len(new_arr)):
    for j in range(i):
        if new_arr[i] < new_arr[j]:
            new_arr[i], new_arr[j] = new_arr[j], new_arr[i]

print(new_arr)