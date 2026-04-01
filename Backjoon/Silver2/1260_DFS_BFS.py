def dfs(s):
    if visited[s]:
        return

    visited[s] = 1
    ans.append(s)
    for i in sorted(adj_list[s]):
        dfs(i)


def bfs(s):
    queue = [s]

    while queue:
        current = queue.pop(0)
        if visited[current]:
            continue

        visited[current] = 1
        ans.append(current)
        for i in sorted(adj_list[current]):
            queue.append(i)



N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = []

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

dfs(V)
print(*ans)
visited = [0] * (N+1)
ans = []
bfs(V)
print(*ans)
