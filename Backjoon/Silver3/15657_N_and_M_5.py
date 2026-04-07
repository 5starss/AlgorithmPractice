def recur(cnt=0):
    if cnt == M:
        print(*answer)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            answer.append(arr[i])
            recur(cnt+1)
            visited[i] = 0
            answer.pop()

    return

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
visited = [0] * N
arr.sort()

recur()