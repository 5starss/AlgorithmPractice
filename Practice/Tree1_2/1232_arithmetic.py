# 아직 미완

import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    adj_list = [[] for _ in range(N+1)]
    tree = [0] * (N+1)

    for _ in range(N):
        arr = list(input().split())
        if arr[1].isdigit():
            tree[int(arr[0])] = int(arr[1])
        else:
            tree[int(arr[0])] = arr[1]

        for i in arr[2:]:
            adj_list[arr[0]].append(i)

