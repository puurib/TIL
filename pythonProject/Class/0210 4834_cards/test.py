N= 5
numbers = list(map(int, input()))
# print(numbers)
cards = [0] * 50

# number에서 나온 수를 1씩 더함.
for num in numbers:
    cards[num] += 1
print(cards)

# 가장 큰 수 찾기
maxnum = cards[0]
max_i= 0
for i in range(50):
    if maxnum <= cards[i]:
        maxnum = cards[i]
        print(maxnum, i)
        max_i = i
print(f'#{max_i} {maxnum}')