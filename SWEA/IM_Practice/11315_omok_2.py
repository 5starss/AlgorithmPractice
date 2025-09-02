def garo_sero():
    for i in range(N):
        for j in range(N-5+1):
            if arr[i][j:j+5] == ['o', 'o', 'o', 'o', 'o']:
                return True

    arr2 = list(map(list, zip(*arr)))
    for i in range(N):
        for j in range(N-5+1):
            if arr2[i][j:j+5] == ['o', 'o', 'o', 'o', 'o']:
                return True
    return False


def cross():
    for i in range(2, N-2):
        for j in range(2, N-2):
            if arr[i][j] == 'o' and arr[i-2][j-2] == 'o' and arr[i-1][j-1] == 'o' and arr[i+1][j+1] == 'o' and arr[i+2][j+2] == 'o':
                return True
            elif arr[i][j] == 'o' and arr[i+2][j-2] == 'o' and arr[i+1][j-1] == 'o' and arr[i-1][j+1] == 'o' and arr[i-2][j+2] == 'o':
                return True
    return False


def omok():
    if garo_sero():
        return True

    if cross():
        return True

    return False


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = "NO"
    if omok():
        ans = "YES"

    print(f"#{tc} {ans}")
