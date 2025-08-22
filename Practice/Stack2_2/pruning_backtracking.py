def f(i, N):
    global cnt
    if i == N:
        s = 0
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == key:
            cnt += 1
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = list(range(1, 10))
N = 10
key = 10
bit = [0] * 10
cnt = 0

f(0, N)


