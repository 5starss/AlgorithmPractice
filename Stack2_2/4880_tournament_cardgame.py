#분할 정복

def RSP(a, b):
    if (arr[a-1] == 1 and arr[b-1] == 2) or (arr[a-1] == 2 and arr[b-1] == 3) or (arr[a-1] == 3 and arr[b-1] == 1):
        return b
    else:
        return a

def winner(i, j):
    if i == j:
        return i
    else:
        left = winner(i, (i+j)//2)
        right = winner((i+j)//2 + 1, j)
        return RSP(left, right)

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = winner(1, N)
    print(f"#{tc} {ans}")

