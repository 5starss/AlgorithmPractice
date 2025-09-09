def candy(A, B, C):
    global eat
    if C < 3 or B < 2:
        eat = -1
        return

    if B >= C:
        eat += B-C+1
        B = C-1

    if A >= B:
        eat += A - B + 1


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    eat = 0

    candy(A, B, C)

    print(f"#{tc} {eat}")



