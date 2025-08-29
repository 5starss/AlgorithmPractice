def heap_push(item):
    heap.append(item)
    idx = len(heap) - 1
    while idx > 1 and heap[idx] < heap[idx//2]:
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        idx //= 2


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]
    ans = 0

    # 부모: n//2, 최소힙 -> 부모 < 자식
    for i in range(N):
        heap_push(arr[i])

    last = N
    while last > 1:
        last //= 2
        ans += heap[last]

    print(f"#{tc} {ans}")
