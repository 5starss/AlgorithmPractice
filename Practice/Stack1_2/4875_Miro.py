def DFS_stack(miro, x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    stack = [(x,y)]

    while stack:
        current_x, current_y = stack.pop()

        if miro[current_x][current_y] == 3:
            return 1

        miro[current_x][current_y] = 1

        for d in range(4):
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and miro[nx][ny] in (0, 3):
                stack.append((nx, ny))

    return 0


def DFS_recursive(miro, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    if miro[x][y] == 3:
        return 1

    miro[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N and miro[nx][ny] in (0, 3):
            if DFS_recursive(miro, nx, ny) == 1:  # 재귀함수의 핵심. 한번 리턴 1이 되었다면 끝날때까지 1만 리턴
                return 1
    return 0


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                x = i
                y = j

    # ans = DFS_stack(miro, x, y)

    ans = DFS_recursive(miro, x, y)

    print(f"#{tc} {ans}")


