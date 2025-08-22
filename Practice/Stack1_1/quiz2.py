import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str_ = input()

    stack = []

    ans = 1
    for s in str_:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                ans = -1
    if stack:
        ans = -1

    print(f"#{tc} {ans}")
