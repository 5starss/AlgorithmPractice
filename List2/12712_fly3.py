import sys
sys.stdin = open('input.txt', 'r')

def kill_fly_plus(x, y, N, M):  # 십자가 접근
    dx = [0, 1, 0, -1]  # 이동할 값. 십자가
    dy = [1, 0, -1, 0]

    sum_kill = arr[x][y]  # 원점 포함
    for i in range(4):
        for m in range(1, M):  # 세기만큼 접근. M = 3인 경우 원점 포함 3칸이므로 2칸만 더 가면 됨.
            nx = x + dx[i] * m
            ny = y + dy[i] * m
            if 0 <= nx < N and 0 <= ny < N:
                sum_kill += arr[nx][ny]
    return sum_kill

def kill_fly_x(x, y, N, M):  # 대각선 접근
    dx = [1, 1, -1, -1]  # 이동할 값. 대각선
    dy = [1, -1, 1, -1]

    sum_kill = arr[x][y]
    for i in range(4):
        for m in range(1, M):  # 세기
            nx = x + dx[i] * m
            ny = y + dy[i] * m
            if 0 <= nx < N and 0 <= ny < N:
                sum_kill += arr[nx][ny]

    return sum_kill


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N):
        for j in range(N):
            max_kill = max(max_kill, kill_fly_plus(i, j, N, M), kill_fly_x(i, j, N, M))  # 최대값 갱신

    print(f"#{tc} {max_kill}")
