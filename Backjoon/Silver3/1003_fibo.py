T = int(input())
for _ in range(T):
    N = int(input())
    fibo = [1, 1]
    # 점화식
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        for _ in range(N-2):
            fibo[0], fibo[1] = fibo[1], fibo[0]
            fibo[1] += fibo[0]

        print(*fibo)