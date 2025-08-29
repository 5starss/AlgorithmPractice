def level_order(root):
    q = [root]

    while q:
        parent = q.pop(0)
        print(str_[parent], end='')

        for i in adj_list[parent]:
            q.append(i)


def inorder(root):
    if root:
        inorder(adj_list[root][0])
        print(str_[root], end='')
        inorder(adj_list[root][1])


def postorder(root):
    for i in adj_list[root]:
        inorder(i)
    print(str_[root], end='')


import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())

    adj_list = [[0, 0] for _ in range(N+1)]
    str_ = [0] * (N+1)
    parent = [0] * (N+1)

    for i in range(1, N+1):
        arr = list(input().split())
        for j in range(len(arr)):
            if j == 1:
                str_[i] = arr[j]
            elif j > 1:
                if adj_list[i][0] == 0:
                    adj_list[i][0] = int(arr[j])
                else:
                    adj_list[i][1] = int(arr[j])
                parent[int(arr[j])] = i

    root = 0
    for i in range(1, N + 1):
        if parent[i] == 0:
            root = i
    print(f"#{tc}", end=' ')
    inorder(root)
    print()