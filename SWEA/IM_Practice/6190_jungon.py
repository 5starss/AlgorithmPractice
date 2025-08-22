def is_monotonic_increasing(int_):
    str_ = str(int_)
    for i in range(len(str_)-1):
        if str_[i] > str_[i+1]:
            return False
    return True

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_ = 0
    ans = -1
    for i in range(N-1):
        for j in range(i+1, N):
            if is_monotonic_increasing(arr[i] * arr[j]) and arr[i] * arr[j] > ans:
                ans = arr[i] * arr[j]
    print(f"#{tc} {ans}")