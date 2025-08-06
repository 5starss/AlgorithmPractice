import sys

sys.stdin = open('input.txt', 'r')

def sum_x(x, y, N, M):  # 대각선 접근
    dx = [1, 1, -1, -1]  # 이동할 값. 대각선
    dy = [1, -1, 1, -1]

    sum_ = arr[x][y]
    for i in range(4):
        for m in range(1, M):  # 세기
            nx = x + dx[i] * m
            ny = y + dy[i] * m
            if 0 <= nx < N and 0 <= ny < N:
                sum_ += arr[nx][ny]

    return sum_

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ''' 교재대로
    sum_ = 0
    for i in range(N):
        sum_ += arr[i][i]  # 왼위 -> 오아 대각선 합
        sum_ += arr[i][N - 1 - i]  # 오위 -> 외아 대각선 합

    sum_ -= arr[N//2][N//2]  # 홀수는 가운데 겹치는 부분이 있음

    print(f"#{tc} {sum_}")
    '''
    # 델타 사용. N이 홀수일 때만 가능
    M = N // 2 + 1  # 대각선 길이
    sum_ = sum_x(N // 2, N // 2, N, M)  # 중앙 index -> (x, y)
    print(f"#{tc} {sum_}")
