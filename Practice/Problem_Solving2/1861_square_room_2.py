def delta(x, y, cnt):
    global ans, room
    start = arr[x][y]
    queue = [(x, y, cnt)]
    while queue:
        x, y, cnt = queue.pop(0)

        if cnt > ans:
            ans = cnt
            room = start
        elif cnt == ans:
            room = min(start, room)

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and arr[x][y]+1 == arr[nx][ny]:
                queue.append((nx, ny, cnt+1))


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    room = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            delta(i, j, 1)

    print(f"#{tc} {room} {ans}")
