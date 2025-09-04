import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    min_ = N
    for i in range(N-2):
        for j in range(i+1, N-1):
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                size = [i+1, j-i, N-j-1]

                if any(k > N//2 for k in size):
                    continue

                min_ = min(min_, (max(size) - min(size)))

    if min_ == N:
        min_ = -1
    print(f"#{tc} {min_}")
