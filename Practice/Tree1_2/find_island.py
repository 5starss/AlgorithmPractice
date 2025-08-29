"""
5 5
11000
11000
00000
00101
01001
"""
def DFS_delta(x, y):
    # 상하좌우+대각선, 총 8 방향 확인
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        arr[x][y] = 2  # 확인 여부 저장

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                stack.append((nx, ny))

def BFS_delta(x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)

        arr[x][y] = 2  # 확인 여부 저장

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                queue.append((nx, ny))


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(5)]
ans = 0

# 전체 탐색
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            # DFS_delta(i, j)
            # BFS_delta(i, j)
            ans += 1

print(ans)