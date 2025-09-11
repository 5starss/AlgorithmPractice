import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        l, r = 0, N-1
        direction = -1
        while l <= r:
            mid = (l+r)//2
            if A[mid] > b:
                if direction != 0:
                    direction = 0
                    r = mid-1
                else:
                    break
            elif A[mid] < b:
                if direction != 1:
                    direction = 1
                    l = mid+1
                else:
                    break
            else:
                cnt += 1
                break

    print(f"#{tc} {cnt}")
