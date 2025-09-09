def bfs(R, C):
    global ans

    queue = [(R, C, 1)]
    visited[R][C] = 1

    while queue:
        current_r, current_c, cnt = queue.pop(0)
        ans += 1

        if cnt == L or arr[current_r][current_c] == 0:
            continue

        for dx, dy in dict_[arr[current_r][current_c]]:
            nx = current_r + dx
            ny = current_c + dy

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] != 1:
                if dx == 1 and arr[nx][ny] in (1, 2, 4, 7):
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
                elif dx == -1 and arr[nx][ny] in (1, 2, 5, 6):
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
                elif dy == 1 and arr[nx][ny] in (1, 3, 6, 7):
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
                elif dy == -1 and arr[nx][ny] in (1, 3, 4, 5):
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 0

    dict_ = {
        1: [(0,1), (1,0), (0,-1), (-1,0)],
        2: [(1,0), (-1,0)],
        3: [(0,1), (0,-1)],
        4: [(-1,0), (0,1)],
        5: [(1,0), (0,1)],
        6: [(1,0), (0,-1)],
        7: [(0,-1), (-1,0)]
    }

    bfs(R, C)

    print(f"#{tc} {ans}")