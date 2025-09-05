def dfs(x, y, sum_):
    global ans
    if x == N-1 and y == N-1:
        ans = min(ans, sum_)
    if x < N-1:
        dfs(x+1, y, sum_ + arr[x+1][y])
    if y < N-1:
        dfs(x, y+1, sum_ + arr[x][y+1])

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_ = [[0] * N for _ in range(N)]
    sum_[0][0] = arr[0][0]
    for i in range(1, N):
        sum_[i][0] = arr[i][0] + sum_[i-1][0]
        sum_[0][i] = arr[0][i] + sum_[0][i-1]

    for i in range(1, N):
        for j in range(1, N):
            sum_[i][j] = min(sum_[i-1][j], sum_[i][j-1]) + arr[i][j]

    print(f"#{tc} {sum_[N-1][N-1]}")

    ans = 260
    dfs(0, 0, arr[0][0])

    print(f"#{tc} {ans}")
