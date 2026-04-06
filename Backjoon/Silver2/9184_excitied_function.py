dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

# 미리 다 구해서 적용
for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b < c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

# calculated = [[[0]*21 for i in range(21)] for j in range(21)] 를 사용하여 그때그때 계산도 가능

while True:
    a, b, c = map(int, input().split())
    answer = 0
    if a == -1 and b == -1 and c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        answer = 1
    elif a > 20 or b > 20 or c > 20:
        answer = dp[20][20][20]
    else:
        answer = dp[a][b][c]

    print(f"w({a}, {b}, {c}) = {answer}")
