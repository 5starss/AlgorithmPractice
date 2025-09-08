import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)

    ans = 0

    for i in range(M):
        for j in range(len(w)):
            if w[j] <= t[i]:
                ans += w[j]
                w.pop(j)
                break

    print(f"#{tc} {ans}")
