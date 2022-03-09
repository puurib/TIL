import random

lotto_lst = [1, 23, 29, 33, 37, 40]
bonus_num = 16

for _ in range(1000):
    my_lotto = random.sample(range(1, 45),6)

# 밑에 이거를 천번 돌리면 될듯..

cnt= 0
for i in range(len(lotto_lst)):
    if lotto_lst[i] in my_lotto:
        cnt += 1

rlt = ''
if cnt == 6:
    rlt = "1등"
elif cnt == 5:
    if bonus_num in my_lotto:
        rlt ="2등"  
    else:
        rlt ="3등"
elif cnt == 4:
    rlt ="4등"
elif cnt == 3:
    rlt = "5등"
else:
    rlt = "꽝"

print(rlt)