def check(x, y, n):
    color = arr[y][x]
    for i in range(n):
        for j in range(n):
            if arr[y+i][x+j] != color:
                check(x, y, n // 2)
                check(x, y + n // 2, n // 2)
                check(x + n // 2, y, n // 2)
                check(x + n // 2, y + n // 2, n // 2)
                return
    else:
        ans[color] += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans= [0, 0]

check(0, 0, n)
for i in ans:
    print(i)