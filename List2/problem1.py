import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_ = 0
    for i in range(N):
        sum_ += arr[i][i]  # 왼위 -> 오아 대각선 합
        sum_ += arr[i][N - 1 - i]  # 오위 -> 외아 대각선 합

    sum_ -= arr[N//2][N//2]  # 홀수는 가운데 겹치는 부분이 있음

    print(f"#{tc} {sum_}")