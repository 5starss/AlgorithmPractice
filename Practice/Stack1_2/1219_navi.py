def DFS_stack(start, end):
    stack = [start]
    visited = [0] * (99+1)

    while stack:
        current = stack.pop()

        if current == end:
            return 1

        visited[current] = 1

        for next in range(99, -1, -1):
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                stack.append(next)

    return 0


def DFS_recursive(start, end):
    if start == end:
        return 1

    visited[start] = 1

    for next in range(99, 0, -1):
        if adj_matrix[start][next] == 1 and visited[next] == 0:
            if DFS_recursive(next, end) == 1:
                return 1

    return 0

import sys

sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_matrix = [[0] * 100 for _ in range(100)]

    for i in range(N):
        adj_matrix[arr[i*2]][arr[i*2+1]] = 1

    ans = DFS_stack(0, 99)

    visited = [0] * 100
    # ans = DFS_recursive(0, 99)
    print(f"#{tc} {ans}")

