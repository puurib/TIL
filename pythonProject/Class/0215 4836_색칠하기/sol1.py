'''
4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
예를 들어 책이 총 400쪽이면,
검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.


해결 방식
1. 문제 정보에 따라서 10 * 10을 초기화해둔다.
2. 색상 정보의 인덱스를 사용해서 행, 열을 구한다.
3. 2의 행열 값을 사용해서 색상이 없다면 색상값을 넣어주고,
색상이 있다면 보라색 중복값과 같은 색상값이 없는 경우로 조건을 적어줬다.
4. color = 1 (빨강), color = 2 (파랑)을 더한 3이 되는 경우만 cnt로 개수를 셌다.

어려웠던 점
1. input.txt를 보니까 같은 색상이 여러 번 들어오는 경우에는 어떻게 해야할지 몰랐는데
    for i in range(N):
        info[i] = list(map(int, input().split()))
   위 코드 처럼 처럼 for문을 사용해서 미리 초기화해둔 info(색상 정보)의 원소로 사용했다.

2. 보라색은 color = 1 (빨강), color = 2 (파랑)을 더한 3으로 처리하였다.
3. 색상이 이미 있을 경우에는 어떻게 해야할지 헷갈렸다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input()) # 도형의 개수
    full = [[0]*10 for _ in range(10)] # 10 * 10 격자무늬 초기화
    cnt = 0  # 보라색 개수
    info = [[0]*5 for _ in range(N)] # 색상 정보
    for i in range(N):
        info[i] = list(map(int, input().split())) #색상 정보를 저장
        
    #print(info)
    
    for color in info:
        for row in range(color[0], color[2]+1): # 이게 행이 됨
            for column in range(color[1], color[3]+1): # 이게 열이 됨
                # 색상이 지정되지 않았다면 색상을 지정해주고 color = 1 (빨강), color = 2 (파랑)
                if full[row][column] == 0:
                    full[row][column] += color[4]
                    
                # 중복이 아니거나, 다른 색이 칠해져있는 경우에만 보라색 개수 cnt를 추가해준다.
                elif full[row][column] !=3 and full[row][column] != color[4]:
                    full[row][column] = 3
                    cnt +=1
    
    print(f'#{tc} {cnt}')
                
