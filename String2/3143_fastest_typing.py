import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = input().strip().split()
    N = len(A)
    M = len(B)

    i = 0

    cnt = 0
    # while i < N:
    #     j = 0
    #     while i < N and j < M:
    #         if B[j] != A[i]:
    #             i -= j
    #             j = -1
    #         i += 1
    #         j += 1
    #     if j == M:
    #         cnt += 1

    for i in range(N-M+1):
        for j in range(M):
            if A[i+j] != B[j]:
                break
        else:
            cnt += 1

    print(f"#{tc} {N - ((M-1)*cnt)}")
