'''
패턴찾기
'''
def is_pattern():
    map_arr = [['A', 'B', 'G', 'K'], ['T', 'T', 'A', 'B'], ['A', 'C', 'C', 'D']]
    pattern_arr = [list(input()) for _ in range(2)]
    #pattern_arr = [['A','B'], ['C', 'D']]
    cnt = 0

    for i in range(len(map_arr)):
        for j in range(len(map_arr[0])-1): #0,1,2까지 돌아야
            if map_arr[i][j:j+2]==pattern_arr[0] or map_arr[i][j:j+2]==pattern_arr[1]:
                cnt += 1

    if cnt == 0:
        rlt = '미발견'
    else:
        rlt = f'발견({cnt})개'

    return rlt

print('"'+f'{is_pattern()}'+'"')
