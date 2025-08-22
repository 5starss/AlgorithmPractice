import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N, str = input().split()
    stack = []  # 스택 생성
    for s in str:  # 각 문자 확인
        if stack:  # 스택에 값이 있는 경우
            temp = stack.pop()  # 바로 이전 문자 뽑아서 확인. 반복 문자는 지워짐
            if temp != s:  # 지금 문자와 다른 경우, 반복 문자가 아닌 경우
                stack.append(temp)  # 확인한 문자 다시 넣기
                stack.append(s)  # 확인한 문자 넣기
        else:  # 스택에 값이 없는 경우
            stack.append(s)  # 값 넣기
    print(f"#{tc} {''.join(stack)}")
