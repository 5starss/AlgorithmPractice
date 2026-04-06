H, W, N, M = map(int, input().split())

answer = ((H+N) // (N+1)) * ((W+M) // (M+1))

print(answer)