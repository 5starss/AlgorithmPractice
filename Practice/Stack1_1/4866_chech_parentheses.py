import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    test = input()
    stack = []
    ans = 1  # 초기값. 괄호에 문제가 없는 경우 그대로 출력
    for char in test:
        if char == '{' or char == '(':  # 열린 괄호 확인. 스택에 넣는 조건
            stack.append(char)
        elif char == '}':  # 괄호 닫기 확인
            if stack:  # 열린 괄호가 있는 경우
                if stack.pop() != '{':  # 괄호 짝이 아닌 경우
                    ans = 0
            else:  # 열린 괄호가 없는 경우
                ans = 0
        elif char == ')':
            if stack:
                if stack.pop() != '(':
                    ans = 0
            else:
                ans = 0
    if stack:  # 열린 괄호가 남아 있는 경우
        ans = 0

    print(f"#{tc} {ans}")

# class Stack:
#     def __init__(self, size):
#         self.size = size  # 스택 크기
#         self.capacity = [None] * size  # 길이만큼 배열 생성
#         self.top = -1  # top 포인터 초기값
#
#     def is_empty(self):  # 비어있는지 확인
#         return self.top == -1
#
#     def push(self, item):  # 값 넣기
#         if self.top == self.size - 1:  # 꽉 차있다면 메세지 리턴
#             return "Stack Overflow"
#         self.top += 1
#         self.capacity[self.top] = item
#
#     def pop(self):  # 값 빼기
#         if self.is_empty():  # 스택이 비어있을 경우 메세지 리턴
#             return "Stack Underflow"
#         self.top -= 1
#         return self.capacity[self.top + 1]  # 값 리턴
#
#     def peek(self):  # 가장 위에 있는 값 확인
#         if self.is_empty():  # 스택이 비어있을 경우 메세지 리턴
#             return "Stack is empty"
#         return self.capacity[self.top]  # 값 리턴
#
#     def matching(self, string):
#         ans = 1
#         for char in string:
#             if char == '{' or char == '(':
#                 self.push(char)
#             elif char == '}':
#                 if not self.is_empty():
#                     if self.pop() != '{':
#                         ans = 0
#                 else:
#                     ans = 0
#             elif char == ')':
#                 if not self.is_empty():
#                     if self.pop() != '(':
#                         ans = 0
#                 else:
#                     ans = 0
#         if not self.is_empty():
#             ans = 0
#         return ans
#
# import sys
#
# sys.stdin = open('input.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     str_ = input()
#     stack = Stack(len(str_))
#     ans = stack.matching(str_)
#
#     print(f"#{tc} {ans}")