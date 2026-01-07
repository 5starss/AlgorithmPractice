"""
5 7
4 5 1 3 2
"""

def merge(left, right):
    global cnt, ans
    tmp_list = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            tmp_list.append(left[l])
            l += 1
        else:
            tmp_list.append(right[r])
            r += 1

    while l < len(left) and cnt < K:
        tmp_list.append(left[l])
        l += 1

    while r < len(right) and cnt < K:
        tmp_list.append((right[r]))
        r += 1

    for i in tmp_list:
        if cnt < K:
            ans = i
            cnt += 1

    return tmp_list

def merge_sort(li):
    if len(li) == 1:
        return li

    mid = (len(li)+1) // 2
    left_li = merge_sort(li[:mid])
    right_li = merge_sort((li[mid:]))

    return merge(left_li, right_li)

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
ans = 0
merge_sort(arr)
if cnt < K:
    ans = -1

print(ans)