def back(N, M, arr, current=1, cnt=0):
    if current > N:
        return

    if cnt >= M:
        print(" ".join(arr))
        return

    for i in range(current, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(str(i))
            back(N, M, arr, i, cnt+1)
            visited[i] = 0
            arr.pop()

    return

N, M = map(int, input().split())
visited = [0] * (N+1)
ans = []
back(N, M, ans)