def know_key(node, arr):
    stack = [node]

    while stack:
        current = stack.pop()

        visited[current] = 1

        for next_ in arr[current]:
            if visited[next_] == 0:
                stack.append(next_)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = int(input())

    adj_list = [[] for _ in range(N+1)]
    parent = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        parent[b].append(a)

    cnt = 0
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        know_key(i, adj_list)
        know_key(i, parent)
        print(visited)
        if 0 not in visited[1:N+1]:
            cnt += 1

    print(f"#{tc} {cnt}")
