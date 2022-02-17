import sys
sys.stdin = open('input.txt', encoding='utf-8')

for _ in range(1, 11):
    t = int(input())
    p = input()
    sentence = input()

    #개수를 세어줄 변수
    cnt = 0
    
    #주어진 문장을 p의 길이만큼 순차적으로 확인하면서 p와 일치하면 cnt 1 증가
    for i in range(len(sentence)-len(p)+ 1):
        if p == sentence[i:i+len(p)]:
            cnt += 1
    
    print(f'#{t} {cnt}')