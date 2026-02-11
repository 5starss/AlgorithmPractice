N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for i in range(1, N+1):
    ans += sum(arr[0:i])

print(ans)