
T = int(input())
for tc in range(1, T+1):

    N, S = input().split()
    n = int(N)
    word = ''
    for i in range(len(S)):
        word += S[i] * n

    print(word)