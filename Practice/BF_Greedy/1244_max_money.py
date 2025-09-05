def swap(arr, cnt):
    global ans
    if max_ == ans:
        return

    if cnt == int(E):
        ans = max(ans, int(''.join(arr)))
        return

    arr2 = arr[:]

    for i in range(len(arr2)-1):
        for j in range(len(arr2)):
            if i != j:
                arr2[i], arr2[j] = arr2[j], arr2[i]
                swap(arr2, cnt+1)
                arr2[i], arr2[j] = arr2[j], arr2[i]


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num, E = input().split()

    ans = 0
    num_list = list(num)

    max_ = int("".join(sorted(num, key=lambda x: int(x), reverse=True)))
    swap(num_list, 0)

    print(f"#{tc} {ans}")

