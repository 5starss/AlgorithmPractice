from collections import deque

N, K = map(int, input().split())

queue = deque([(N, 0)])
visited = [100000] * 100001
ans = 100000
visited[N] = 1
while queue:
    pos, cnt = queue.popleft()

    if pos == K:
        ans = min(ans, cnt)
        continue

    if ans <= cnt:
        continue

    cnt += 1

    if pos + 1 < 100001 and visited[pos+1] > cnt:
        visited[pos+1] = cnt
        queue.append((pos+1, cnt))
    if pos - 1 >= 0and visited[pos-1] > cnt:
        visited[pos-1] = cnt
        queue.append((pos-1, cnt))
    if pos * 2 < 100001 and  visited[pos * 2] > cnt:
        visited[pos*2] = cnt
        queue.append((pos*2, cnt))

print(ans)

