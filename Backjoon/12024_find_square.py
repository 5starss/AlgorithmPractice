N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

queue = []
for i in range(N):
    queue.append([i])

while queue:
    cycle = queue.pop(0)

    if len(cycle) < 4:
        for i in range(N):
            if arr[cycle[-1]][i] == 1 and (i not in cycle):
                cycle.append(i)
                tmp = cycle[:]
                queue.append(tmp)
                cycle.pop()
    else:
        # print(f"cycle[-1]: {cycle[-1]}, arr[cycle[-1]][0]: {arr[cycle[-1]][0]}")
        # print(arr)
        # print(arr[cycle[-1]][cycle[0]])
        if arr[cycle[-1]][cycle[0]] == 1:
            cnt += 1
            # print(f"cnt: {cnt}")

print(cnt)


