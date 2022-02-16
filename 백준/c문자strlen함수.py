

def strlen(arr):
    str_a = ''
    idx = 0
    while idx < len(arr):
        if arr[idx] != '\0':
            str_a += arr[idx]
        idx +=1
            
    return len(str_a)

a = ['a', 'b', 'c', '\0']
print(strlen(a))