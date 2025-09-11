def binary_search(l, r, key, direction=-1):
    global cnt
    # 방향 0 = 왼, 1 = 오
    if l > r:
        return

    mid = (l+r)//2
    if key < A[mid]:
        if direction != 0:
            binary_search(l, mid-1, key, 0)
    elif key > A[mid]:
        if direction != 1:
            binary_search(mid+1, r, key, 1)
    else:
        cnt += 1
        return


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        binary_search(0, N-1, b)

    print(f"#{tc} {cnt}")

