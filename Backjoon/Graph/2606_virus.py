N = int(input())
V = int(input())

adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = 0

for _ in range(V):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

queue = [1]

while queue:
    current = queue.pop(0)

    if visited[current]:
        continue

    visited[current] = 1
    ans += 1
    for i in adj_list[current]:
        if not visited[i]:
            queue.append(i)

print(ans-1)