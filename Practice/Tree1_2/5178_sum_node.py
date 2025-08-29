import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        i, n = map(int, input().split())
        tree[i] = n

    last = N
    if last % 2 == 0:
        tree[last//2] = tree[last]
        last -= 1

    while last > 1:
        tree[last//2] = tree[last] + tree[last-1]
        last -= 2

    print(f"#{tc} {tree[L]}")

