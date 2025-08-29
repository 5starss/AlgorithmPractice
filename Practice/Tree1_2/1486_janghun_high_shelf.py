def recursive(start, sum_=0):
    global ans

    if sum_ >= B:
        ans = min(ans, sum_ - B)

    if start < N:
        sum1 = sum_
        sum2 = sum1 + arr[start]

        recursive(start+1, sum1)
        recursive(start+1, sum2)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = sum(arr)

    recursive(0)

    print(f"#{tc} {ans}")

