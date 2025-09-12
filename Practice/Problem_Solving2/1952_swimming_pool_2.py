import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    p_daily, p_month, p_months, p_year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    ans = p_year
    memo = [0] * 13

    memo[1] = min(arr[1]*p_daily, p_month)
    memo[2] = memo[1] + min(arr[2]*p_daily, p_month)
    for i in range(3, 13):
        memo[i] = min(memo[i-1] + arr[i]*p_daily, memo[i-1] + p_month, memo[i-3] + p_months)

    print(f"#{tc} {min(memo[-1], p_year)}")
