'''
4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

해결 방식
1. 일단 리스트를 정렬한다. 오름차순으로 버블 정렬을 해줬음
2. 큰수 -> 작은수 -> 큰수 -> 작은수..를 인덱스를 이용해서 처리함
3. 10개까지 슬라이싱해서 출력

어려웠던 점
1. 리스트를 str형식으로 만들기 위해서 join을 써줬다..
2. 이문제상으론 10개까지 끊어서 출력해서 정수 N이 짝/홀수인지 여부는 중요치 않았는데,
전체를 출력했다면 짝/홀수 여부로 나눠서 처리했어야 했음. --> 하지만 나는 안했음..
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N= int(input())
    number_lst = list(map(int, input().split()))
    rlt = []
    #print(f'{tc} {number_lst}')

    # 리스트 정렬하기 (오름차순)
    for i in range(N):
        for j in range(i):
            if number_lst[i] <= number_lst[j]:
                number_lst[j], number_lst[i] = number_lst[i], number_lst[j]

    # 리스트에서 큰수 작은수 .......까지
    for i in range(N):
        if i == int(N/2):
            break
        else:
            rlt.append(number_lst[-1 - i])
            rlt.append(number_lst[i])

    # 10개까지 잘라내기
    result = ' '.join(map(str, rlt[0:10]))
    print(f'#{tc} {result}')