import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    boong = 0
    ans = 'Possible'
    for i in range(max(arr)+1):
        if i > 0 and i % M == 0:
            boong += K

        if i in arr:
            a = arr.count(i)
            if boong < a:
                ans = 'Impossible'
                break
            boong -= a

    print(f"#{tc} {ans}")






