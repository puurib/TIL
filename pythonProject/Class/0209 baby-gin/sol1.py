# baby-gin

import sys
sys.stdin = open('input.txt')

def check_babygin(numbers):
    counter = [0] * 10 # 각 숫자를 카운트할 리스트
    is_babygin = 0 # 정답 여부 ~~~~> is_뫄뫄 : 라고 변수명을 많이 짓는다!

    # 0-9의 카드 개수 세기
    for number in numbers:
        counter[number] += 1
    # 조건이 두개여서 while을 씀
    idx = 0
    while idx < len(counter): #모든 카드를 돌겠어

        # check triplet
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue
        # check run
        if idx < len(counter) -2: #
            if counter[idx] and counter[idx+1] and counter[idx+2]: # 모두 true
                counter[idx] -= 1
                counter[idx + 1] -= 1
                counter[idx + 2] -= 1
                is_babygin += 1
                continue
        idx += 1

    # 결과 체크
        if is_babygin == 2:
            return 1
    return 0 # (중요)

T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int. input()))
    result = check_babygin(numbers)
    print(f'#{tc}({result})')