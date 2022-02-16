from msilib import datasizemask


arr = [["A","B","C"],["A","G","H"],["H","I","J"],["K","A","B"],["A","B","C"]]

# 1. 버켓 배열 만들기

dat = [0] * 200 # 아스키코드 값 넣기 위해 넉넉하게 

for row in range(5):
    for col in range(3):
        dat[ord(arr[row][col])] += 1

for i in range(len(dat)):
    if dat[i] >= 1:
        print(chr(i)*dat[i], end='')
    