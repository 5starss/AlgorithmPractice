def is_palindrome(arr):
    return arr==arr[::-1]

import sys

sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    ans = 0
    
    # 100x100 탐색
    for i in range(100):
        for j in range(100-ans):
            for k in range(99, ans, -1):  # 글자수가 큰 것부터 탐색
                if j + k < 101 and is_palindrome(arr[i][j:j+k]):  # 회문인가?
                    ans = k
                    break  # 글자수가 큰 것부터 탐색하기 때문에 처음 나온게 가장 긴 길이

    # 전치
    arr2 = list(zip(*arr)) 

    for i in range(100):
        for j in range(100-ans):
            for k in range(99, ans, -1):
                if j + k < 101 and is_palindrome(arr2[i][j:j + k]):
                    ans = k
                    break

    print(f"#{tc} {ans}")
