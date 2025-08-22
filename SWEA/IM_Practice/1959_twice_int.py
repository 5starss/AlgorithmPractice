import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_ = 0
    if N < M:
        for i in range(M-N+1):
            tmp = 0
            for j in range(N):
                tmp += A[j] * B[i+j]
            max_ = max(max_, tmp)

    else:
        for i in range(N-M+1):
            tmp = 0
            for j in range(M):
                tmp += A[i+j] * B[j]
            max_ = max(max_, tmp)

    print(f"#{tc} {max_}")
