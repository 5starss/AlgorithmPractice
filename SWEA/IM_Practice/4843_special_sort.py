import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        if N % 2 == 1:
            max_idx = i
            for j in range(i+1, N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            min_idx = i
            for j in range(i+1, N):
                if arr[min_idx] < arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f"#{tc}", *arr)
