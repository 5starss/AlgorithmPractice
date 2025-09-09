import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_list = [[0] * M for _ in range(N)]
    ans = 0
    water_list = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                water_list.append((i, j))

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                for x, y in water_list:
                    if min_list[i][j] == 0:
                        min_list[i][j] = abs(i - x) + abs(j - y)
                    else:
                        min_list[i][j] = min((abs(i-x) + abs(j-y)), min_list[i][j])

    # print(min_list)
    print(f"#{tc} {sum(number for row in min_list for number in row)}")
