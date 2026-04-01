import sys

input = sys.stdin.readline

def check(mid, M):
    sum_ = 0
    for i in arr:
        if mid < i:
            sum_ += (i - mid)
        if sum_ >= M:
            return True

    return False


N, M = map(int, input().split())

arr = list(map(int, input().split()))
max_ = max(arr)
min_ = 0
ans = 0

while max_ >= min_:
    mid = (max_ + min_) // 2

    if check(mid, M):
        ans = mid
        min_ = mid + 1
    else:
        max_ = mid - 1

print(ans)




