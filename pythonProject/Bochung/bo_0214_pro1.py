arr = [3, 6, 5, 8, 5, 3, 5, 8, 5, 3, 3, 1, 1, 3]
pattern = [3, 5, 8, 4]

# arr 배열안에 pattern이 존재하는지 존재 여부를 출력
for i in range(len(arr) - 4):
    if arr[i] == pattern[0] and arr[i + 1] == pattern[1] and arr[i + 2] == pattern[2] and arr[i + 3] == 5:
        print('존재함')
    else:
        print('존재하지 않음')