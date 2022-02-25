infix = "(6+5*(2-8)/2)"
stack = [] # 변환을 위해 사용할 스택
result = [] # 결과가 담길 스택

# 1. 중위표현식을 순회
for token in infix:

    # 2. 만약에, 니가 숫자라면 결과에 push
    if token.isdigit():
        result.append(token)

    else:  # 연산자라면
        if not stack: #스택이 비어있다면
            stack.append(token)
        else: # 스택이 비어있지 않다면 (icp, isp 비교후 push)

            # icp = 3
            if token == "(":
                stack.append(token)
            elif token == ")":
                temp = stack.pop()
                while temp != "(":
                    result.append(temp)
                    temp = stack.pop()

            # icp = 2
            elif token == "*"  or token == "/":
                # stack이 차있고 가장 높은 게 *이거나 /이라면
                while stack and stack[-1] == "*" or stack[-1] == "/":
                    result.append(stack.pop())
                # /를 만났을때 /보다 낮은건 다 빼주고 /을 넣어주는 코드
                stack.append(token)

            # icp = 1
            elif token == "+" or token == "-":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.append(token)

# stack에 남아있다면, 모두 꺼내서 push
for token in range(len(stack)):
    result.append(stack.pop())


print(infix)
print(result)
