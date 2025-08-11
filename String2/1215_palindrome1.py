def is_palindrome(arr):
    return arr==arr[::-1]

import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            if is_palindrome(arr[i][j:j+N]):
                cnt += 1

    arr2 = list(zip(*arr))

    for i in range(8):
        for j in range(8-N+1):
            if is_palindrome(arr2[i][j:j+N]):
                cnt += 1

    print(f"#{tc} {cnt}")
