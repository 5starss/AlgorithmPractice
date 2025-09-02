def road(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = [(x, y)]

    cnt = 1
    while queue:
        x, y = queue.pop(0)

        tmp_x, tmp_y = x, y
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[tmp_x][tmp_y] > arr[nx][ny]:
                    tmp_x, tmp_y = nx, ny

        if arr[tmp_x][tmp_y] != arr[x][y]:
            queue.append((tmp_x, tmp_y))
            cnt += 1

    return cnt


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_ = 0
    for i in range(N):
        for j in range(N):
            cnt = road(i, j)
            max_ = max(max_, cnt)

    print(f"#{tc} {max_}")
