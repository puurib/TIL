arr = [3, 6, 5, 8, 5, 3, 5, 8, 5, 3, 3, 1, 1, 3]
pattern = [3, 5, 8, 4]
pattern_lst = []
# arr 배열안에 pattern이 존재하는지 존재 여부를 출력
for i in range(len(arr) - len(pattern)):
    is_pattern = arr[i:i+len(pattern)]
    pattern_lst.append(is_pattern)

if pattern in pattern_lst:
    print('존재함')
else:
    print('존재하지 않음')