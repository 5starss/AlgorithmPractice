def sum_path(arr):
    sum_ = 0
    for i in range(N):
        sum_ += adj_mat[arr[i]-1][arr[i+1]-1]
    return sum_


def recur(cnt):
    global ans

    if cnt == N-1:
        total_path = [1]
        total_path.extend(path)
        total_path.append(1)

        ans = min(ans, sum_path(total_path))
        return

    for i in range(2, N+1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        recur(cnt+1)
        path.pop()
        used[i] = False


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    adj_mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 1000
    path = []
    used = [False] * (N+1)

    recur(0)

    print(f"#{tc} {ans}")
