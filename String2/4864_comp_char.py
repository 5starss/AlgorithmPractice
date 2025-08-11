import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str2)
    M = len(str1)

    ans = 0
    # while문
    # i, j = 0, 0
    # while i < len(str2) and j < len(str1):
    #     if str1[j] != str2[i]:
    #         i -= j
    #         j = -1
    #     i += 1
    #     j += 1
    # if j == len(str1):
    #     ans = 1

    # for문
    for i in range(N-M+1):
        for j in range(M):
            if str2[i+j] != str1[j]:
                break
        else:
            ans = 1

    print(f"#{tc} {ans}")
