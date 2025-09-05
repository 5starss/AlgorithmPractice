def dfs(cnt, sum_):
    global ans
    if sum_ > 10:
        return

    if cnt == 3:
        ans += 1
        return

    for i in range(1, 7):
        dfs(cnt+1, sum_+i)


ans = 0

dfs(0, 0)

print(ans)
