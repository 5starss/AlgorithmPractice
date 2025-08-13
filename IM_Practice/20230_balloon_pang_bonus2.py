import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # dx = [0, 1, 0, -1]
    # dy = [1, 0, -1, 0]
    #
    # max_ = 0
    # for x in range(N):
    #     for y in range(N):
    #         cnt = arr[x][y]
    #
    #         for p in range(1, N):
    #             for d in range(4):
    #                 nx = x + dx[d] * p
    #                 ny = y + dy[d] * p
    #
    #                 if 0 <= nx < N and 0 <= ny < N:
    #                     cnt += arr[nx][ny]
    #
    #         max_ = max(max_, cnt)
    max_ = 0
    arr2 = list(zip(*arr))
    for x in range(N):
        for y in range(N):
            sum_ = sum(arr[x])
            sum_ += sum(arr2[y])
            sum_ -= arr[x][y]
            max_ = max(max_, sum_)

    print(f"#{tc} {max_}")
