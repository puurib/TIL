# 0209 SWEA 1206 VIEW 문제!

import sys
sys.stdin = open('input.txt')

T = 10 # 열개라고 주어짐

for tc in range(1, T + 1):
    cnt = int(input()) # 빌딩 수를 받는다.
    builings = list(map(int, input().split())) # 빌딩 높이
    
    ans = 0 # 조망권이 확보된 세대
    # 1. 모든 빌딩을 돈다
    for i in range(2, cnt-2):
        curr_height = builings[i] # curr_height 현재 높이

        if not curr_height: # 빌딩이 안지어진 곳이라면 다시 for문 돌아
            continue
        else:
            max_height= 0  # max_height = 이번 빌딩을 기준으로 한 빌딩 중 가장 높은 높이

            # 중요합니다아아아아ㅏ 양 옆 두칸씩의 빌딩 높이 구하기 idx기준으로
            d_col = [-2, -1, 1, 2] #델타 = 변화량 / 미리 만들어두고
            for d in d_col: # 그 인덱스를 체크하겠다..
                check_idx = i + d # check_idx = 양옆 두칸의 빌딩의 인덱스
                # 양 옆 두칸 빌딩의 높이 구하기
                if builings[check_idx] >= max_height:
                    max_height = builings[check_idx]

            if curr_height > max_height: # 조망권이 확보된 경우
                ans += curr_height - max_height
    print(f'#{tc} {ans}')