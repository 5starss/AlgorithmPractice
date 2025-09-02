import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    half = (N+1)//2
    ans = []

    i = 0
    while i < half:
        ans.append(arr[i])
        if i + half < N:
            ans.append(arr[i+half])
        i += 1

    print(f"#{tc}", *ans)

