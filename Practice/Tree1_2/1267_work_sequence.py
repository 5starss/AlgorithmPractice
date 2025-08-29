def is_ready(num):
    for i in parent[num]:
        if ready[i] != 1:
            return False

    return True

def bfs(roots):
    queue = roots

    while queue:
        current = queue.pop(0)

        if not is_ready(current):
            queue.append(current)
            continue

        if ready[current] == 1:
            continue

        ready[current] = 1
        print(current, end=' ')

        for i in adj_list[current]:
            if ready[i] == 0:
                queue.append(i)



import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [[] for _ in range(V+1)]
    ready = [0] * (V+1)  # 작업 실행 여부 확인

    adj_list = [[] for _ in range(V + 1)]

    for i in range(E):
        adj_list[arr[2*i]].append(arr[2*i+1])
        parent[arr[2*i+1]].append(arr[2*i])
    print(adj_list)
    roots = []

    for i in range(1, V+1):
        if not parent[i]:
            roots.append(i)

    print(f"#{tc}", end=' ')
    bfs(roots)
    print()
