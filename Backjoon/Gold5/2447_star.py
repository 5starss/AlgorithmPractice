def star(x, y, l):
    l //= 3

    if ans[x][y] == ' ' or l == 0:
        return

    for j in range(l, l*2):
        for k in range(l, l*2):
            ans[x+j][y+k] = ' '

    for j in range(0, 3):
        for k in range(0, 3):
            star(x + j * l, y + k * l, l)


N = int(input())

ans = [['*' for _ in range(N)] for _ in range(N)]
star(0, 0, N)
for i in range(N):
    print(''.join(ans[i]))
