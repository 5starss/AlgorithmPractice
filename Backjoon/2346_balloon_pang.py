from collections import deque

N = int(input())
arr = list(map(int, input().split()))

q = deque()
for i, j in enumerate(arr):
    q.append((i+1, j))

while q:

    i, j = q.popleft()
    print(i, end=' ')
    if j > 0:
        q.rotate(-(j-1))
    else:
        q.rotate(-(j))

print()



