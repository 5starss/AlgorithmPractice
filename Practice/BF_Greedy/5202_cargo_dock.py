import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[-1])
    start = arr[0][-1]
    cnt = 1
    for i in range(1, N):
        if start <= arr[i][0]:
            start = arr[i][1]
            cnt += 1

    print(f"#{tc} {cnt}")