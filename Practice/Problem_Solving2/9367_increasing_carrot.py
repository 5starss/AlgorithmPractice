import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 1
    tmp = 1
    for i in range(N-1):
        if tmp + N - i - 1 < ans:
            break

        if arr[i] < arr[i+1]:
            tmp += 1
        else:
            tmp = 1
        ans = max(ans, tmp)

    print(f"#{tc} {ans}")