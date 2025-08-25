import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr= list(map(int, input().split()))

    cnt = 0
    max_ = arr[-1]
    ans = 0
    for i in range(N-1, -1, -1):
        if max_ > arr[i]:
            ans += max_ - arr[i]
        else:
            max_ = arr[i]

    print(f"#{tc} {ans}")

