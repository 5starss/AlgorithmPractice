def switch_(arr, n):
    for i in range(n, len(arr)):
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 0


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if A[i] != B[i]:
            switch_(A, i)
            cnt+=1

        if A == B:
            break

    print(f"#{tc} {cnt}")