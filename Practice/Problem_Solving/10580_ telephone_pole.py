import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(N)])
    # ans = 0
    # for i in range(N - 1):
    #     for j in range(i + 1, N):
    #         if arr[i][1] > arr[j][1]:
    #             ans += 1
    ans = sum(1 for i in range(N - 1) for j in range(i + 1, N) if arr[i][1] > arr[j][1])
    print(f"#{tc} {ans}")

