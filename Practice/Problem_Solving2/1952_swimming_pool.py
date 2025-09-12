def recur(month, sum_):
    if month > 11:
        month = 12
        dp[month] = min(dp[month], sum_)
        return

    if sum_ >= dp[month]:
        return

    dp[month] = sum_

    if arr[month] == 0:
        recur(month + 1, sum_)
    else:
        recur(month + 1, sum_ + arr[month] * p_daily)
        recur(month + 1, sum_ + p_month)
        recur(month + 3, sum_ + p_months)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    p_daily, p_month, p_months, p_year = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [p_year] * 13

    recur(0, 0)

    print(f"#{tc} {dp[-1]}")