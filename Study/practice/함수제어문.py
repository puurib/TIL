
# P1
students = ['김철수', '이영희', '조민지']

# 아래에 코드를 작성하시오.
print(len(students))


# P2
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 아래에 코드를 작성하시오.
cnt = 0

# for idx in range(len(students)):
#     if students[idx] == '이영희':
#         cnt += 1

for student in students:
    if student == '이영희':
        cnt += 1
print(cnt)


# P3
numbers = [7, 10, 22, 4, 3, 17]

n = -987654321
for number in numbers:
    if number > n:
        n = number
print(n)

# P4
numbers = [7, 10, 22, 4, 3, 17]

n = 987654321
for number in numbers:
    if number < n:
        n = number
print(n)

# n = numbers[0]
# for number in numbers:
#     if number < n:
#         n = number
# print(n)


# P5
numbers = [7, 10, 22, 7, 22, 22]

n = numbers[0]
for number in numbers:
    if number > n:
        n = number

# 최대값이 n에 저장되어있음
cnt = 0
for number in numbers:
    if number == n:
        cnt += 1

print(n, cnt)

# P6
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

cnt = 0
for num in numbers:
    if num == 5:
        cnt += 1
print(cnt)

######### while
# i = 0
# five = 0
# while i < len(numbers):
#     if numbers[i] == 5:
#         five += 1
#     i += 1
# print(five)



# P7
word = input()
rlt_str = ''

# for ch in word:
#     if ch == 'a':
#         continue # pass
        # ~~~~~~~~~~~~
#     else:
#         rlt_str += ch

for ch in word:
    if ch != 'a':
        rlt_str += ch

print(rlt_str)


# P8
word = input()
print(word[::-1])


# for i in range(1,6):
#         print(word[5-i], end="")





