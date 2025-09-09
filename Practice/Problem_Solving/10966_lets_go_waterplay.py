from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque([(i, j, 0)])
    visited = [[0] * M for _ in range(N)]

    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = 1

        if dp[x][y] != 1e9:
            dp[i][j] = min((dp[x][y] + cnt), dp[i][j])
            continue

        if arr[x][y] == 'W':
            dp[i][j] = min(dp[i][j], cnt)
            return dp[i][j]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                queue.append((nx, ny, cnt+1))
                visited[nx][ny] = 1

    return dp[i][j]

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = 0
    dp = [[1e9] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                if dp[i][j] == 1e9:
                    ans += bfs(i, j)
                else:
                    ans += dp[i][j]

    # print(dp)
    print(f"#{tc} {ans}")