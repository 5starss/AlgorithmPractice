T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_ = 0 # 최대 낙차

    for j in range(N-1):
        cnt = 0  # 낙차
        for k in range(j+1, N):
            if arr[j] > arr[k]:
                cnt += 1  # 이후 값들이 나보다 작을 경우 +1

        if max_ < cnt:
            max_ = cnt
    print(f"#{i} {max_}")