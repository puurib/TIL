'''
4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스'
첫 줄엔 T = 노선 (tc)의 개수
다음줄엔 각 노선별로 K, N, M이 주어지고,
(K = 최대이동가능한 정류장수, N= 총 정류장 수, M= 충전기 설치된 정류장 수)
numbers = 다음줄에 M개의 정류장 번호가 주어진다.
최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    max_move, total_busstop, charge_num = map(int, (input().split()))
    numbers = list(map(int, input().split())) # 충전기 설치된 정류장 리스트

    # 1. 0 -> total_busstop 까지 가야하는데, 최대 이동거리는 max_move이다.
    # 2. charge_num은 충전기가 설치된 정류장의 수, numbers는 충전기가 설치된 정류장 리스트이다.
    
    # 3. 우선 0, 1로 체크할 수 있는 리스트를 만들고 numbers와 비교해서 설치된 곳만 1로 표시!
    check_lst = [0] * total_busstop
    for number in numbers:
        check_lst[number] += 1
    # print(check_lst) 
    
    # 4. check_lst 를 돌면서, max_move만큼 가봄, 충전기를 만나면 충전,
    for i in range(total_busstop):
        i

    # 5. max_move에 충전기가 없다면 -1씩 뒤로 back해서 충전하고 그 위치부터 다시 출발.
    
    # 6. 5에서 이전 max_move 값 까지 아예 없으면 0을 출력해줄 것
    
    print(f'#{tc} {check_lst}')