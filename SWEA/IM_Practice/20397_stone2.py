def flip(arr, n):
    if arr[n] == 0:
        arr[n] = 1
    else:
        arr[n] = 0


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))  # 초기상태
    for _ in range(M):
        i, j = map(int, input().split())

        for x in range(1, j+1):
            if 0 <= i-1-x < N and 0 <= i-1+x < N:
                if arr[i-1+x] == arr[i-1-x]:
                    flip(arr, i-1+x)
                    flip(arr, i-1-x)

    print(f"#{tc}", *arr)

