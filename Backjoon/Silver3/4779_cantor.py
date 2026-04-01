def cantor(l, r):
    i, j = int(l+(r-l)/3), int(l+2*(r-l)/3)
    if i == j or i <= l or j >= r:
        return

    for k in range(i, j):
        ans[k] = ' '

    cantor(l, i)
    cantor(j, r)

while 1:
    try:
        N = int(input())
        l, r = 0, 3**N

        ans = ['-'] * r
        if not N:
            print('-')
        else:
            cantor(l, r)

            ans = ''.join(ans)
            print(ans)
    except EOFError:
        break