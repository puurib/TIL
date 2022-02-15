arr=[[3,4,1],[4,5,2],[3,8,3]]

arr_sum = 0
max_sum = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr_sum += arr[i][j]
        #print(arr_sum)

        if arr_sum > max_sum:
            max_sum = arr_sum

print(f'{max_sum}')