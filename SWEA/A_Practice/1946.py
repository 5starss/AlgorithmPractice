import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = []
    for _ in range(N):
        char, num = map(str, input().split())
        arr.extend([char] * int(num))

    print(f"#{tc}")
    while arr:
        i = 0
        while i < 10 and arr:
            print(arr.pop(0), end='')
            i += 1
        print()

