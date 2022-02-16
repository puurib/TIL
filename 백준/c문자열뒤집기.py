'''
문자열 뒤집기 방법
1. 슬라이싱
2. reverse() --> None 반환주의, 원본 리스트가 정렬되는 것임.
3. 새로운 문자열 생성
3-1. 인덱스(처음부터) + 빈문자 --> 어색한 사용법이다..잘알아두기
'''

# 1. 슬라이싱
def slicing(word):
    reverse_word = word[::-1]
    return reverse_word

# 2. reverse()를 사용
# def func_reverse(word):
#     word_list = list(word)
#     reverse_word = word_list.reverse()
#     return reverse_word
#print(func_reverse(s))  ---> 자꾸 None이 나옴.. 왜일까?


def func_reverse(word):    
    word_list = list(word)
    new_word = ''
    word_list.reverse() # TypeError: 'NoneType' object is not iterable
    for i in word_list:
        new_word += i
    
    return new_word

#s = 'Reverse this strings'
#print(func_reverse(s))


# 3. 새로운 문자열 생성
def new_str1(word):
    new_word = ''
    for idx in s[::-1]:
        new_word += idx
    return new_word
#print(new_word)


# 3-1. 새로운 문자열 생성
def new_str2(word):
    new_word = ''
    for c in word:
        new_word = c + new_word
    return new_word


s = 'Reverse this strings'
print(f'#1 슬라이싱 방법: {slicing(s)}')  #1 슬라이싱 방법: sgnirts siht esreveR
print(f'#2 reverse 사용: {func_reverse(s)}') #2 reverse 사용: sgnirts siht esreveR 
print(f'#3 새로운 문자열: {new_str1(s)}') #3 새로운 문자열: sgnirts siht esreveR
print(f'#4 인덱스 + 빈문자: {new_str2(s)}') #4 인덱스 + 빈문자: sgnirts siht esreveR

print('------------------------------------------')
