def parents(i):
    parents_arr = [i]

    while parent[i] != 0:
        parents_arr.append(parent[i])
        i = parent[i]

    return parents_arr


def tree_size(root):
    size = 0

    stack = [root]

    while stack:
        node = stack.pop()
        size += 1

        for i in adj_list[node]:
            stack.append(i)

    return size


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [0] * (V + 1)

    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        adj_list[arr[2 * i]].append(arr[2*i+1])
        parent[arr[2 * i + 1]] = arr[2 * i]

    parent1 = parents(n1)
    parent2 = parents(n2)

    same_parent = 0
    for p in parent1:
        if p in parent2:
            same_parent = p
            break

    ans = tree_size(same_parent)

    print(f"#{tc} {same_parent} {ans}")
