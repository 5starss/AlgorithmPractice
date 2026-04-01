from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        current_x, current_y = queue.popleft()
        cnt = ans[current_y][current_x]

        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and ans[ny][nx] > cnt + 1:
                ans[ny][nx] = cnt + 1
                queue.append((nx, ny))



n, m = map(int, input().split())
max = n * m
mat = [list(map(int, input().split())) for _ in range(n)]
ans = [[max] * m for _ in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            x, y = j, i
            ans[i][j] = 0
        elif mat[i][j] == 0:
            ans[i][j] = 0

bfs(x, y)

for i in range(n):
    for j in range(m):
        if ans[i][j] == max:
            ans[i][j] = -1

for i in ans:
    print(*i)

