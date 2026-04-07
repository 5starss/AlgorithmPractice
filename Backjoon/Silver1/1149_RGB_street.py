N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_ = [[1000*N, 1000*N, 1000*N] for _ in range(N)]

for i in range(1, N):
    for j in range(3): # i 줄
        for k in range(3): # i-1 줄
            if j != k:
                min_[i][j] = min(min_[i][j], arr[i][j] + arr[i-1][k])
        arr[i][j] = min_[i][j]

print(min(arr[-1]))
