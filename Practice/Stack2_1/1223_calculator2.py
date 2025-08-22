import sys

sys.stdin = open('input.txt', 'r')

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    stack = []
    result = ''

    for token in expression:
        if token.isalnum():  # 괄호, 연산자가 아닌 경우
            result += token
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':  # '('를 만날 때까지 pop
                result += stack.pop()
            stack.pop()  # '('도 제거
        else:  # 연산자
            # 우선순위 비교 후 토큰의 우선순위가 더 높지 않은 경우
            # precedence에 없는 경우는 이들보다 우선순위가 높은 경우(거듭제곱 등)
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                result += stack.pop()
            stack.append(token)

    while stack:  # 다 끝난 후 스택에 남아있는 결과물 pop
        result += stack.pop()

    return result


def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():  # 연산자가 아닌 경우
            stack.append(int(token))  # push
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                res = a + b
            elif token == '-':
                res = a - b
            elif token == '*':
                res = a * b
            elif token == '/':
                res = a / b
            elif token == '^':
                res = a ** b
            else:
                raise ValueError(f"잘못된 토큰입니다.: {token}")

            # 계산 결과를 다시 push
            stack.append(res)

            # 최종 스택에 남은 값이 결과
    return stack.pop()

for tc in range(1, 11):
    N = input()
    expression = input()
    ans = infix_to_postfix(expression)
    ans2 = evaluate_postfix(ans)
    print(f"#{tc} {ans2}")