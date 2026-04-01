# 배열을 만들 경우
# 재귀 없이 푸는 방법
N, r, c = map(int, input().split())
a = 0
M = 2 ** N

x, y = 0, 0

while M > 1:

    M //= 2
    if c < x + M and r < y + M:
        pass
    elif x + M <= c and r < y + M:
        a += M ** 2
        x += M
    elif c < x + M and y + M <= r:
        a += (M ** 2) * 2
        y += M
    else:
        a += (M ** 2) * 3
        x += M
        y += M

print(a)


""" 재귀로 푸는 방법
def recur(x, y, M):
    global a, r, c

    if M == 1:
        if y == r and x == c:
            print(a)
            exit()
        a += 1
        return

    if x > c or c > x + M or y > r or r > y + M:
        a += M ** 2
        return

    M //= 2
    recur(x, y, M)
    recur(x+M, y, M)
    recur(x, y+M, M)
    recur(x+M, y+M, M)
    return

N, r, c = map(int, input().split())
a = 0
M = 2 ** N

recur(0, 0, M)

print(a)
"""

