arr=[[3,4,1],[4,5,2],[3,8,3]]

arr_sum = 0

for i in range(-len(arr), 1, 1):

    arr_sum += arr[i][i]

print(arr_sum)