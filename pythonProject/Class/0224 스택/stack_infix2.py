result = "6528-*2/+"
stack = []

for token in result:
    if token.isdecimal():
        stack.append(int(token))

    else: # 연산자를 만난경우
        p2 = stack.pop()   # 중요한 것은 p2, p1순으로 팝하는 것 ..순서중요
        p1 = stack.pop()

        if token == "+":
            rlt = p1 + p2
            stack.append(rlt)
        elif token == "-":
            rlt = p1 - p2
            stack.append(rlt)
        elif token == "*":
            rlt = p1 * p2
            stack.append(rlt)
        elif token == "/":  # 만약  /할때 p2가 0이라면,, 처리도 해줄수있지만 여기서는 안함
            rlt = p1 / p2
            stack.append(rlt)

ans = stack.pop()
print(ans)