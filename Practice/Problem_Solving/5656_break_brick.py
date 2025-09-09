from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def shoot(cnt, remains, now_arr):
    global min_blocks
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    for col in range(W):
        copy_arr = [row[:] for row in now_arr]
        row = -1
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break

        if row == -1:
            continue

        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remains - 1
        copy_arr[row][col] = 0

        while q:
            r, c, p = q.popleft()
            for k in range(1, p):
                for i in range(4):
                    nr = r + dy[i] * k
                    nc = c + dx[i] * k

                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    if copy_arr[nr][nc] == 0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        for c in range(W):
            idx = H - 1  # 벽돌이 위치할 index
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(cnt + 1, now_remains, copy_arr)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9
    blocks = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    shoot(0, blocks, arr)
    print(f'#{tc} {min_blocks}')

