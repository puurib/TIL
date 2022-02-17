import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    tc, N = input().split()
    words = input().split()
    lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    my_dict = {}
    for elem in lst:
        my_dict[elem] = 0

    for word in words:
        my_dict[word] += 1