import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = input().strip().split()

    i = 0

    cnt = 0
    while i < len(A):
        j = 0
        while i < len(A) and j < len(B):
            if B[j] != A[i]:
                i -= j
                j = -1
            i += 1
            j += 1
        if j == len(B):
            cnt += 1

    print(f"#{tc} {len(A) - ((len(B)-1)*cnt)}")
