import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # P : 전체 쪽수, pa : a가 찾아야할 쪽수 pb: b가 찾아야할 쪽수
    P, pa, pb = map(int, input().split())
    # print(f'{tc} {P} {pa} {pb}')
    papb = [pa, pb]  # 리스트로 만들어줬음
    cnt = [0, 0]  # 횟수 초기화

    for i in range(2):
        end = P
        start = 1
        while start <= end:
            center = (start + end) // 2  # 중간 페이지
            if papb[i] == center:
                break
            elif papb[i] < center:  # end, start의 바뀌는 값 주의
                end = center
            elif papb[i] > center:
                start = center
            cnt[i] += 1
        # print(cnt[i]) 1 2 9 9 7 8
        # print(cnt)
    if cnt[0] > cnt[1]:  # 누가 이기는지 경우의 수를 나눠줌
        print(f'#{tc} B')
    elif cnt[0] < cnt[1]:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')  # 비긴 경우는 0으로 처리
