def is_omok(x, y, cnt):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for d in range(8):
        nx, ny = x, y
        cnt = 1
        while cnt < 5:
            nx = nx + dx[d]
            ny = ny + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'o':
                    cnt += 1
                else:
                    break
            else:
                break
        else:
            return True

    return False

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    ans = "NO"
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if is_omok(i, j, 1):
                    ans = "YES"

    print(f"#{tc} {ans}")
