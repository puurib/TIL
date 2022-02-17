def itoa(my_int):
    my_str = ""  # 이게 리턴 값
    while my_int != 0:
        # 나머지를 구해서
        r = my_int % 10
        # 나머지를 문자열로 만들고, my_str에 더해줌
        my_str = chr(ord("0") + r) + my_str
        # 나눈 몫을 다시 my_int에 저장
        my_int //= 10

    return my_str


user_number = int(input())  # 정수
print(type(user_number))
print(type(itoa(user_number)))  # class_str
print(itoa(user_number))