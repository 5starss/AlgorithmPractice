def recur(current, cnt, sum_):
    global ans
    if sum_ >= ans:
        return

    if cnt == N:
        sum_ += adj_mat[current][0]
        ans = min(ans, sum_)
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            recur(i, cnt+1, sum_+adj_mat[current][i])
            used[i] = 0


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    adj_mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 1000
    used = [0] * N
    used[0] = 1
    recur(0, 1, 0)

    print(f"#{tc} {ans}")
