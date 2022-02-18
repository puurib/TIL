'''
1859. 백만 장자 프로젝트

해결 방식
1.

어려웠던 점
1.

'''

import sys
sys.stdin = open('input.txt')

T = int(input()) # tc수 = 3

for tc in range(1, T + 1):
    N = int(input()) # 들어올 값 리스트의 원소 수, 쉽게 말해 값들의 리스트
    price = list(map(int, input().split()))


    # 필요한 것 : 최대값, 사기, 팔기, 총이익 변수가 필요할 것 같고
    # 일차원 리스트를 이용해서 조작해봐야할듯.
    # 사기 : 내 뒤의 값이 나보다 더 크면 물건 살거야, 작으면 안사
    # 팔기 : 내가 최대값이라면 내 앞의 개수만큼 팔거고 최대값인 날은 안삼
    # 총이익 : (최대값 - 그날의 가격 ) 누적.

    buy = 0
    sell = 0
    max_price = 0
    benefit = 0
    buy_lst = []
    # 최대값

    for i in range(len(price)-2):
        if price[i] < price[i+1]:
            buy += 1
            buy_lst.append(price[i])
            #print(buy_lst)

        elif price[i] >= price[i+1]:
            # buy X
            if buy > 0:
                for j in buy_lst:
                    benefit += price[i] - j
                    buy_lst = []
            else:
                continue

    print(f'#{tc} {benefit}')






