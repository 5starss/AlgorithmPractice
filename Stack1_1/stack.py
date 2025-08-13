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
#         if self.top == self.size-1:  # 꽉 차있다면 메세지 리턴
#             return "Stack Overflow"
#         self.top += 1
#         self.capacity[self.top] = item
#
#     def pop(self):  # 값 빼기
#         if self.is_empty():  # 스택이 비어있을 경우 메세지 리턴
#             return "Stack Underflow"
#         self.top -= 1
#         return self.capacity[self.top+1]  # 값 리턴
#
#     def peek(self):  # 가장 위에 있는 값 확인
#         if self.is_empty():  # 스택이 비어있을 경우 메세지 리턴
#             return "Stack is empty"
#         return self.capacity[self.top]  # 값 리턴

