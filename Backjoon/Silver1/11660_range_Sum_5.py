import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N+1)]
sum_ = [[0] * (N+1) for _ in range(N+1)]  # 누적 합((0,0)부터의 네모)

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append([0] + row)

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_[i][j] = sum_[i][j-1] + sum_[i-1][j] - sum_[i-1][j-1] + arr[i][j] # (0,0)부터의 네모

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum_[x2][y2] - sum_[x2][y1-1] - sum_[x1-1][y2] + sum_[x1-1][y1-1]  # 네모 구하기

    print(ans)
