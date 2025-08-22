def DFS_stack(start, end):
    stack = [start]
    visited = [0] * (V+1)

    while stack:
        current = stack.pop()

        if current == end:
            return 1

        visited[current] = 1

        for next in range(V, 0, -1):
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                stack.append(next)

    return 0


def DFS_recursive(start, end):
    if start == end:
        return 1

    visited[start] = 1

    for next in range(V, 0, -1):
        if adj_matrix[start][next] == 1 and visited[next] == 0:
            if DFS_recursive(next, end) == 1:
                return 1

    return 0


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_matrix = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        i, j = map(int, input().split())
        adj_matrix[i][j] = 1

    S, G = map(int, input().split())
    # ans = DFS_stack(S, G)

    visited = [0] * (V + 1)
    ans = DFS_recursive(S, G)
    print(f"#{tc} {ans}")



