import sys

sys.stdin = open('input.txt', 'r')

# 델타 이동으로 푸는 법
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]  # 이동할 값
    dy = [1, 0, -1, 0]

    sum_ = 0
    for i in range(N):
        for j in range(N):
            for d in range(4):  # 4방향 이동
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < N:  # 인덱스 에러 방지
                    sum_ += abs(arr[i][j] - arr[ni][nj])  # 연달아 있는 두 값의 차이
    print(f"#{tc} {sum_}")

''' 델타 이동 없이 푸는 법
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_ = 0
    for i in range(N):
        for j in range(N-1):
            sum_ += abs(arr[i][j] - arr[i][j + 1])  # 가로로 연달아 있는 두 값의 차이
    for j in range(N):
        for i in range(N-1):
            sum_ += abs(arr[i][j] - arr[i + 1][j])  # 세로로 연달아 있는 두 값의 차이

    print(f"#{tc} {sum_ * 2}")  # 두 값의 차이를 구하는 부분이 각 두 번씩 필요함
'''