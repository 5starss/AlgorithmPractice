import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # deque 사용
    arr = deque(arr)
    for _ in range(M):
        arr.append(arr.popleft())

    print(f"#{tc} {arr[0]}")

    # 배열 사용
    for _ in range(M):
        arr.append(arr.pop(0))
    print(f"#{tc} {arr[0]}")

    # 규칙 활용
    print(f"#{tc} {arr[M%N]}")
