from collections import deque

def bfs(q):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                visited[i][j] = 0
                q.append((i, j))

    bfs(q)

    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                ans += visited[i][j]

    print(f"#{tc} {ans}")
