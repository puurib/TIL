# 연습 문제 1- 입력받기
'''
33
1 2 3 4 5
3
1 2 3
4 5 6
7 8 9
'''

# number 배열을 만들어 줌.
number = [0]*6
# 6개의 값을 number의 각 원소로 저장해 줌.
# map으로 하면 iterable한 값에 int를 주고 map 오브젝트로 저장해버려서,
# list로 이중 리스트를 만들어 number에 저장함.
# 시간 복잡도 = O(n제곱)
for i in range(0, 6):
    number[i]= list(map(int, input().split()))
for j in number:
    for k in j:
        print(k, end=' ')
    print()