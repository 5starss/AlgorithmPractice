import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    arr += [0]
    start = N-1
    cnt = 0
    while start > 0:
        tmp = 0
        for i in range(start-1, -1, -1):
            if arr[i] >= start-i:
                tmp = i
        start = tmp
        cnt += 1

    print(f"#{tc} {cnt-1}")
