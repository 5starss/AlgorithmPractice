def back(N, M, arr, current=1, cnt=0):
    if cnt >= M:
        print(" ".join(arr))
        return

    for i in range(current, N+1):
        arr.append(str(i))
        back(N, M, arr, i, cnt+1)
        arr.pop()

    return

N, M = map(int, input().split())
visited = [0] * (N+1)
ans = []
back(N, M, ans)