# swea 1208 flatten
'''
00X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
'''

T = 10

for tc in range(1, T+1):
    N = int(input())  # 덤프횟수
    box_lst = list(map(int, input().split()))

    # 각 층마다 몇개가 있는지 카운팅
    cnt = [0] * 101
    for i in box_lst:
        cnt[i] += 1

    # 항상 상자 높이 1 이상 100 이하니까
    min = 101
    max = 0
    for box in box_lst:
        if box < min:
            min = box
        if box > max:
            max = box

    # max 높이에서 1개 빼주고 그걸 min 높이에 더해줌 -> 카운팅이 바뀜
    # 덤프횟수 만큼 반복문 돌려줌
    # 근데 그렇게 하면 min, max 높이가 달라지므로 같이 체크해줌
    n = 0
    while n < N:
        cnt[max] -= 1
        cnt[max-1] += 1
        cnt[min] -= 1
        cnt[min+1] += 1

        # max, min 높이인 애들의 개수가 0개면 안되니까 0 아닐 때까지 찾아서 값 체인지
        while cnt[max] == 0:
            max -= 1
        while cnt[min] == 0:
            min += 1

        n += 1  # while문 빠져나가기 위해서 1씩 더해줌
    result = max - min

    print("#{} {}".format(tc, result))