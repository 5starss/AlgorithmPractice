import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr1))

    longest = 0
    for i in range(N):
        cnt1 = 0
        for j in range(M):
            if arr1[i][j] == 1:
                cnt1 += 1
                longest = max(longest, cnt1)
            else:
                cnt1 = 0

    for i in range(M):
        cnt2 = 0
        for j in range(N):
            if arr2[i][j] == 1:
                cnt2 += 1
                longest = max(longest, cnt2)
            else:
                cnt2 = 0

    if longest == 1:  # 노이즈 판별
        longest = 0

    print(f"#{tc} {longest}")