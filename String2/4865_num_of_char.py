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

# import sys
#
# sys.stdin = open("input.txt", 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     counts = {}
#     for a in str1:
#         counts[a] = 0
#     for b in str2:
#         if b in counts:
#             counts[b] += 1
#
#     max_cnt = 0
#     for k in counts.values():
#         if max_cnt < k:
#             max_cnt = k
#     print(f"#{tc} {max_cnt}")
