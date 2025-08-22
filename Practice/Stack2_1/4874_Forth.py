def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():  # 연산자가 아닌 경우
            stack.append(int(token))  # push
        elif token == '.':
            break
        else:
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                res = a + b
            elif token == '-':
                res = a - b
            elif token == '*':
                res = a * b
            elif token == '/':
                res = a // b
            elif token == '^':
                res = a ** b
            else:
                raise ValueError(f"잘못된 토큰입니다.: {token}")

            # 계산 결과를 다시 push
            stack.append(res)
    if len(stack) > 1:
        return 'error'
    else:
        # 최종 스택에 남은 값이 결과
        return stack.pop()



import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    ans = evaluate_postfix(arr)

    print(f"#{tc} {ans}")