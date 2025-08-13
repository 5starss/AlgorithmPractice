import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    str = input()
    stack = []  # 스택 생성
    arr = ['(', '{', '[', '<']  # 괄호 확인
    ans = 1  # 괄호가 정상적으로 닫힌 경우 그대로 출력
    for s in str:  # 각 문자 확인
        if s in arr:  # 괄호가 열린 경우
            stack.append(s)  # 스택에 추가
        elif s == ')':  # 닫히는 괄호 확인
            if stack:  # 스택에 값이 있는 경우, 열린 괄호가 있는 경우
                if stack.pop() != '(':  # 괄호 짝이 아닌 경우
                    ans = 0
                    break
            else:  # 열린 괄호가 없는 경우
                ans = 0
                break
        elif s == '}':
            if stack:
                if stack.pop() != '{':
                    ans = 0
                    break
            else:
                ans = 0
                break
        elif s == ']':
            if stack:
                if stack.pop() != '[':
                    ans = 0
                    break
            else:
                ans = 0
                break
        elif s == '>':
            if stack:
                if stack.pop() != '<':
                    ans = 0
                    break
            else:
                ans = 0
                break
    else:
        if stack:  # 열린 괄호가 남은 경우
            ans = 0

    print(f"#{tc} {ans}")

# 괄호 리스트 생성
# for tc in range(1, 11):
#     N = int(input())
#     str = input()
#     stack = []  # 스택 생성
#     arr = ['(', '{', '[', '<']  # 열린 괄호 확인
#     arr2 = [')', '}', ']', '>']  # 닫힌 괄호 확인
#     ans = 1  # 괄호가 정상적으로 닫힌 경우 그대로 출력
#     for s in str:  # 각 문자 확인
#         if s in arr:  # 괄호가 열린 경우
#             stack.append(s)  # 스택에 추가
#         elif s in arr2:  # 닫히는 괄호 확인
#             if stack:  # 스택에 값이 있는 경우, 열린 괄호가 있는 경우
#                 if stack.pop() != arr[arr2.index(s)]:  # 괄호 짝이 아닌 경우
#                     ans = 0
#                     break
#             else:  # 열린 괄호가 없는 경우
#                 ans = 0
#                 break
#
#     else:
#         if stack:  # 열린 괄호가 남은 경우
#             ans = 0
#
#     print(f"#{tc} {ans}")
