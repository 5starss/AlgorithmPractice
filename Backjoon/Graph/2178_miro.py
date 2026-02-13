from collections import deque

N, M = map(int, input().split())
mat = [list(map(int, input())) for _ in range(N)]
ans = N * M

queue = deque([(0, 0, 1)])
mat[0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while queue:
    current_x, current_y, cnt = queue.popleft()

    if current_x == M-1 and current_y == N-1:
        ans = min(ans, cnt)
        continue
    else:
        if ans <= cnt:
            continue

    for i in range(4):
        nx = current_x + dx[i]
        ny = current_y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and mat[ny][nx]:
            mat[ny][nx] = 0
            queue.append((nx, ny, cnt+1))

print(ans)