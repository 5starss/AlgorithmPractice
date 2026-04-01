from collections import deque
x = int(input())
ans = x
queue = deque([(x, 0)])
visited = [0] * (x + 1)

while queue:
    current, cnt = queue.popleft()
    visited[current] = 1

    if cnt >= ans:
        continue
    elif current == 1:
        ans = cnt
        continue

    if current % 3 == 0:
        if not visited[current // 3]:
            queue.append((current // 3, cnt + 1))

    if current % 2 == 0:
        if not visited[current // 2]:
            queue.append((current // 2, cnt + 1))

    if not visited[current - 2]:
        queue.append((current - 1, cnt + 1))

print(ans)

""" DP
x = int(input())
dp = [0] * (x + 1)

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[x])
"""