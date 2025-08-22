def is_palindrome(arr):
    return arr==arr[::-1]

import sys

sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    ans = 0

    for i in range(100):
        for j in range(100-ans):
            for k in range(99, ans, -1):
                if j + k < 101 and is_palindrome(arr[i][j:j+k]):
                    ans = k
                    break


    arr2 = list(zip(*arr))

    for i in range(100):
        for j in range(100-ans):
            for k in range(99, ans, -1):
                if j + k < 101 and is_palindrome(arr2[i][j:j + k]):
                    ans = k
                    break


    print(f"#{tc} {ans}")
