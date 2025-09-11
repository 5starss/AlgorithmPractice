def recur(idx, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return

    if idx >= N - 1:
        min_cnt = min(min_cnt, cnt)
        return

    for i in range(arr[idx], 0, -1):
        recur(idx + i, cnt + 1)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)

    min_cnt = N

    recur(0, -1)

    print(f"#{tc} {min_cnt}")