def delta(x, y, str_):
    queue = [(x, y, str_)]
    while queue:
        x, y, str_ = queue.pop(0)

        if len(str_) == 7:
            result.add(str_)
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                queue.append((nx, ny, str_ + arr[nx][ny]))


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        for j in range(4):
            delta(i, j, '')

    print(f"#{tc} {len(result)}")
