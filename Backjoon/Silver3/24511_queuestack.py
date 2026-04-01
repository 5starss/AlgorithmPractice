from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
ans = deque()
for i in range(N-1, -1, -1):
    if A[i] == 0:
        ans.append(B[i])
ans += C
print(*list(ans)[:M])
