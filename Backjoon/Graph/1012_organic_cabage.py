def bug(mat, x, y):
    queue = [(x, y)]
    mat[y][x] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        current_x, current_y = queue.pop(0)

        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and mat[ny][nx]:
                mat[ny][nx] = 0
                queue.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    mat = [[0] * M for _ in range(N)]
    ans = 0

    for _ in range(K):
        x, y = map(int, input().split())
        mat[y][x] = 1

    for j in range(N):
        for i in range(M):
            if mat[j][i] == 1:
                bug(mat, i ,j)
                ans += 1

    print(ans)