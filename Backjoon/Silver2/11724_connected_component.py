from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])
    visited[n] = 1

    while queue:
        current = queue.popleft()

        for i in adj_list[current]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

    return


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = 0

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)

