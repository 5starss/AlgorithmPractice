def trail(x, y, cnt, possible=1):
    global ans
    visited[x][y] = 1

    if cnt > ans:
        ans = cnt
    elif cnt + arr[x][y] < ans:
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if arr[nx][ny] < arr[x][y]:
                visited[nx][ny] = 1
                trail(nx, ny, cnt+1, possible)
                visited[nx][ny] = 0
            else:
                if possible and arr[nx][ny] - K < arr[x][y]:
                    visited[nx][ny] = 1
                    tmp = arr[nx][ny]
                    arr[nx][ny] = arr[x][y]-1
                    trail(nx, ny, cnt+1, 0)
                    visited[nx][ny] = 0
                    arr[nx][ny] = tmp

    visited[x][y] = 0

if __name__ == "__main__":

    import sys

    sys.stdin = open("input.txt", "r")

    T = int(input())
    for tc in range(1, T+1):
        N, K = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]
        visited = [[0] * N for _ in range(N)]
        top = max(map(max, arr))
        ans = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in range(N):
            for j in range(N):
                if arr[i][j] == top:
                    trail(i, j, 1)

        print(f"#{tc} {ans}")