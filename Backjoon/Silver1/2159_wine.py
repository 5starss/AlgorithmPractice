import sys
input = sys.stdin.readline
#
# n = int(input())
# dp = []
# for i in range(n):
#     tmp = int(input())
#     if i == 0:
#         dp.append([tmp, 0])
#     else:
#         dp.append([tmp, tmp+dp[i-1][0]])
#
# dp = [[0,0], [0,0]] + dp
#
# # print(dp)
# if n == 1:
#     print(dp[2][0])
# elif n == 2:
#     print(dp[3][1])
# else:
#     max_arr = [dp[3][1]]
#     for i in range(4, n+2):
#         max_ = max((dp[i-3][0]+dp[i][1]), (dp[i-3][1]+dp[i][1]), (dp[i-2][0]+dp[i][0]), (dp[i-2][1]+dp[i][0]), (dp[i-4][1]+dp[i][1]))
#         # print(max_)
#         max_arr.append(max_)
#         dp[i][1] = max_
#
#     # print(dp)
#     print(max(max_arr))

#-------------------------------------------------------
n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][0] = 0
dp[0][1] = wines[0]
dp[0][2] = 0
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) # 이전 최대값
    dp[i][1] = dp[i-1][0] + wines[i]  # 처음 마시는 경우
    dp[i][2] = dp[i-1][1] + wines[i]  # 연달아서 마시는 경우

print(max(dp[n-1]))