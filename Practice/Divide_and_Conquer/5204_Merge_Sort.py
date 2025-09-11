def merge(left, right):
    global cnt
    tmp_list = []
    l = r = 0

    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            tmp_list.append(left[l])
            l += 1
        else:
            tmp_list.append(right[r])
            r += 1

    while l < len(left):
        tmp_list.append(left[l])
        l += 1

    while r < len(right):
        tmp_list.append((right[r]))
        r += 1

    return tmp_list


def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left_li = merge_sort(li[:mid])
    right_li = merge_sort((li[mid:]))

    return merge(left_li, right_li)

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    arr = merge_sort(arr)

    print(f"#{tc}", arr[N//2], cnt)