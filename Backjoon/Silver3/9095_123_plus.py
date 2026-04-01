def f(N):
    if N == 1:
        return dp[1]
    elif N == 2:
        return dp[2]
    elif N == 3:
        return dp[3]
    else:
        if dp[N-1]:
            return dp[N - 3] + dp[N - 2] + dp[N - 1]
        elif dp[N - 1] and not dp[N - 2]:
            return dp[N - 3] + dp[N - 2] + f(N - 1)
        elif dp[N - 2] and not dp[N - 1]:
            return dp[N - 3] + f(N - 2) + f(N - 1)
        else:
            return f(N - 3) + f(N - 2) + f(N - 1)


T = int(input())
# 이건 모든 테스트 케이스가 dp를 공유하는 상태. 매번 아래서부터 구하는 식으로 해도 시간차이 없음.
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    n = int(input())
    print(f(n))


