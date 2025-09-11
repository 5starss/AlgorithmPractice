def recur(month, sum_):
    global ans

    if month > 11:
        ans = min(ans, sum_)
        return

    if sum_ >= ans:
        return

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
    ans = p_year

    recur(1, 0)

    print(ans)