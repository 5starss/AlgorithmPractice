import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = input()
    cnt = 0  # 조각 개수

    # stack = []  # 스택
    # for i in range(len(arr)):
    #     if arr[i] == '(':  # (이 생길수록 막대기가 생김
    #         stack.append(i)
    #     else:
    #         stack.pop()
    #         if arr[i-1] == ')':  # 앞이 ')'라는 것은 막대기가 끝났다는 것
    #             cnt += 1
    #         elif stack:
    #             cnt += len(stack)

    # 스택을 리스트 대신 정수로 설정
    stack = 0  # 스택 대신
    for i in range(len(arr)):
        if arr[i] == '(':  # (이 생길수록 막대기가 생김
            stack += 1
        else:
            stack -= 1
            if arr[i-1] == ')':  # 앞이 ')'라는 것은 막대기가 끝났다는 것
                cnt += 1
            elif stack:
                cnt += stack

    print(f"#{tc} {cnt}")
