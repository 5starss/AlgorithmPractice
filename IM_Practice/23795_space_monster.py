import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    monster_x, monster_y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                monster_x = i
                monster_y = j

    for d in range(4):
        for p in range(1, N):
            nx = monster_x + dx[d] * p
            ny = monster_y + dy[d] * p

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 1:
                    break
                arr[nx][ny] = 1

    print(f"#{tc} {''.join(map(str, arr)).count('0')}")

