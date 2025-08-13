import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = []

    for money in money_list:
        cnt = 0
        while N - money >= 0:
            N -= money
            cnt += 1
        ans.append(cnt)

    print(f"#{tc}")
    print(*ans)
