N, K = map(int, input().split())
ans = 0
money = []
for _ in range(N):
    money.append(int(input()))
money.reverse()

for i in money:
    if i <= K:
       cnt = K // i
       K -= cnt * i
       ans += cnt

print(ans)