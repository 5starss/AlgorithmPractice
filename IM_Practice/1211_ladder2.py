def len_ladder(arr, j):
    dx = [1, 0, 0]
    dy = [0, 1, -1]
    num = 1
    x = 1
    y = j
    k = 0 # 직진
    while x < 99:
        if k == 0:
            for d in range(1, 3):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:
                    k = d  # 좌우
                    break
        else:
            if arr[x+1][y] == 1:
                k = 0

        x += dx[k]
        y += dy[k]
        num += 1

    return num

import sys

sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    ans = 0
    min_len = 10000
    for i in range(100):
        if ladder[0][i] == 1:
            len_ = len_ladder(ladder, i)
            if min_len > len_:
                min_len = len_
                ans = i
    print(f"{tc} {ans}")


