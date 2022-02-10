# 알고리즘 풀 때 귀찮으니까, txt파일을 넣어서 인풋 값을 받고 제출 할 때는 import ~ txt까지 주석처리하고 제출
import sys

sys.stdin = open('input.txt')
# input 하나에 한 줄!
a, b = map(int, input().split())
# c = int(input())
print(a, b)
#print(c)