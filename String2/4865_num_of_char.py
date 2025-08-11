import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max_ = 0
    for char1 in str1:
        cnt = 0
        for char2 in str2:
            if char1 == char2:
                cnt += 1

        max_ = max(max_, cnt)

    print(f"#{tc} {max_}")
