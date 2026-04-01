from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((j,i))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while queue:
    current_x, current_y =  queue.popleft()

    for i in range(4):
        nx = current_x + dx[i]
        ny = current_y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 0:
            queue.append((nx, ny))
            arr[ny][nx] = arr[current_y][current_x] + 1

for i in range(N):
    for j in range(M):
        if arr[i][j] > ans:
            ans = arr[i][j]
        elif arr[i][j] == 0:
            ans = -1
            break
    if ans == -1:
        break
else:
    ans -= 1

print(ans)
