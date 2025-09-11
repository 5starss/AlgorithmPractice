def recur(sum, cnt):
    global min_cost
    if min_cost <=sum:
        return

    if cnt == N:
        min_cost = min(min_cost, sum)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            recur(sum+arr[cnt][i], cnt+1)
            visited[i] = 0



import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 99*15
    visited = [0] * N
    recur(0, 0)

    print(f"#{tc} {min_cost}")
