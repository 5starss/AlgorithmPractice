def baby_gin(arr):
    arr.sort()
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
            return True
    arr = sorted(list(set(arr)))
    for i in range(len(arr)-2):
        if arr[i] + 1 == arr[i + 1] and arr[i + 1] + 1 == arr[i + 2]:
            return True
    return False

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []

    ans = 0
    for i in range(6):
        p1.append(arr[2*i])
        p2.append(arr[2*i+1])

    print(p1)
    print(p2)
    for i in range(3, 7):
        p1_result = baby_gin(p1[:i])
        p2_result = baby_gin(p2[:i])
        if p1_result and p2_result:
            ans = 1
            break
        elif p1_result:
            ans = 1
            break
        elif p2_result:
            ans = 2
            break

    print(f"#{tc} {ans}")
