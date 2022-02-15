'''
4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

해결 방식
1. 리스트로 순회하는 방식이 익숙하기 때문에 pa,pb(각자 찾아야할 쪽수) 받아서 리스트 형변환을 했음
2. for, while문으로 두 명의 cnt를 더함
3. 2에서, start, end 값이 달라짐을 주의하면서 값을 갱신해줌
4. 각 cnt를 비교하면서 이기고 비기고 진 경우를 나눠서 처리해줌

어려웠던 점
1. 코드의 들여쓰기가 어려웠다.
2. 이진탐색에서 시작값, 끝값이 변경되는 것을 주의하자!
3. 재귀함수로 표현이 가능할 것 같은데 아직 구현법이 어려운 것 같음

[input.txt]
3
400 300 350
1000 299 578
1000 222 888
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # P : 전체 쪽수, pa : a가 찾아야할 쪽수 pb: b가 찾아야할 쪽수
    P, pa, pb = map(int, input().split())
    # print(f'{tc} {P} {pa} {pb}')
    papb = [pa,pb] # 리스트로 만들어줬음
    cnt = [0, 0] # 횟수 초기화
    
    for i in range(2):
        end = P
        start = 1
        while start <= end:
            center = (start + end) // 2  # 중간 페이지
            if papb[i] == center:
                break
            elif papb[i] < center: # end, start의 바뀌는 값 주의
                end = center 
            elif papb[i] > center:
                start = center
            cnt[i] += 1
        # print(cnt[i]) 1 2 9 9 7 8
        #print(cnt)
    if cnt[0] > cnt[1]: # 누가 이기는지 경우의 수를 나눠줌
        print(f'#{tc} B')
    elif cnt[0] < cnt[1]:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0') # 비긴 경우는 0으로 처리

