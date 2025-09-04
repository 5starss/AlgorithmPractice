def recursive(idx, subset):
    global ans
    if idx == 12:
        if len(subset) == N and sum(subset) == K:
            ans += 1
        return
    subset.append(idx + 1)
    recursive(idx+1, subset)
    subset.pop()
    recursive(idx+1, subset)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    arr = list(range(1, 13))
    N, K = map(int, input().split())

    ans = 0

    # for i in range(1 << 12):
    #     subset = []
    #     for j in range(12):
    #         if i & (1 << j):
    #             subset.append(arr[j])
    #     if len(subset) == N and sum(subset) == K:
    #         ans += 1
    #
    # print(f"#{tc} {ans}")

    recursive(0, [])
    print(f"#{tc} {ans}")
