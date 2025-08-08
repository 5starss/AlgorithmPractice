# 'Z'가 존재하는가?
N = int(input())

text = [input() for _ in range(N)]

ans = False
for i in range(N):
    if 'Z' in text[i]:
        ans = True  # 'Z'가 존재

print(ans)
