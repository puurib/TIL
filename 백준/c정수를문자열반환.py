'''
0216 목 연습문제2번 itoa() 함수만들기
아스키 코드가 아닌 **문자열 ‘0~9’ 까지의 index를 활용해서 푸는 방법을 권장**합니다.
양의 정수를 입력받아 문자열로 변환하는 함수를 만들 것

'''

# 받아오는 값이 양의 정수인지 체크
n = 1461
number = list(map(int, n))
print(number)
    # for idx in range(len(number)):
    #     num_str += ''.join(idx)
    # print(num_str, type(num_str))


