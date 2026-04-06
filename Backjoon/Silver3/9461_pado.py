T = int(input())
dp = [1] * 101

for _ in range(T):
    N = int(input())

    if N > 3:
        for i in range(4, N+1):
            if dp[i] != 1:
                continue
            dp[i] = dp[i-3] + dp[i-2]
    print(dp[N])