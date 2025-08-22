import sys
from collections import deque

sys.stdin = open("input.txt", "r")

for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))

    # 배열 사용
    while arr[-1] != 0:
        for i in range(1, 6):
            tmp = arr.pop(0) - i
            if tmp < 0:
                tmp = 0
            arr.append(tmp)

            if tmp == 0:
                break

    print(f"#{tc}", *arr)

    # deque 사용
    arr = deque(arr)
    while arr[-1] != 0:
        for i in range(1, 6):
            tmp = arr.popleft() - i
            if tmp < 0:
                tmp = 0
            arr.append(tmp)

            if tmp == 0:
                break

    print(f"#{tc}", *arr)
