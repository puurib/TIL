'''
2115. [모의 SW 역량테스트] 벌꿀채취
'''
import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    # 벌통들의 크기 N, 선택할 수 있는 벌통의 개수 M, 꿀을 채취할 수 있는 최대 양 C
    N, M, C = map(int, input().split())
    # N*N 개의 벌통에서 채취할 수 있는 꿀의 양에 대한 정보
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {N}')
    pprint(arr)