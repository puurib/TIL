def is_pattern(m, s):

    rlt = ''
#     # a = m[0][2:4]
#     # print(a)    
#     # m 배열에 pattern이 존재하는지 확인하기 - 1개가 발견 되었다면 발견(1개), 없다면 미발견
#     cnt = 0

    for i in m: # 헹 
        if m[i:i+2] == sear_1:
            rlt = f"발견({i}번째 행부터 {i+1}까지)"

    return rlt

map_1 = [['A', 'B', 'G', 'K', 'T', 'T', 'A', 'B']
sear_1 = ['T','A']
ans = is_pattern(map_1, sear_1)
print(ans)