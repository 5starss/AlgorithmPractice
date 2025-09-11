def recur(sum, cnt):
    global max_per
    if max_per >= sum:
        return

    if cnt == N:
        max_per = max(max_per, sum)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            recur(sum*(arr[cnt][i]/100), cnt+1)
            visited[i] = 0

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_per = 0

    recur(1, 0)

    print(f"#{tc} {max_per*100:.6f}")
