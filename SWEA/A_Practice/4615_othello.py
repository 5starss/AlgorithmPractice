def othello(x, y, c):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for d in range(8):
        nx, ny = x, y
        stack = []  # 사이에 끼어있는 다른 돌
        while True:
            nx = nx + dx[d]
            ny = ny + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    break
                elif arr[nx][ny] != c:
                    stack.append((nx, ny))
                elif arr[nx][ny] == c:
                    if stack:
                        while stack:
                            i, j = stack.pop()
                            arr[i][j] = c
                    break
            else:
                break

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2-1][N//2-1], arr[N//2][N//2] = 2, 2
    arr[N//2][N//2-1], arr[N//2-1][N//2] = 1, 1

    for _ in range(M):
        x, y, c = map(int, input().split())  # x, y, color. c=1 -> 흑, 2 -> 백
        arr[x-1][y-1]= c
        othello(x-1, y-1, c)

    cnt_b, cnt_w = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt_b += 1
            elif arr[i][j] == 2:
                cnt_w += 1

    print(f"#{tc} {cnt_b} {cnt_w}")