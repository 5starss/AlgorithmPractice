import sys
input = sys.stdin.readline

def dfs(n):
    stack = [n]
    while stack:
        current = stack.pop()

        for j in adj_list[current]:
            if not parents[j]:
                stack.append(j)
                parents[j] = current

    return

N = int(input())
adj_list = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

dfs(1)

for i in range(2, N+1):
    print(parents[i])
