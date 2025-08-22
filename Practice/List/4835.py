T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_max, sum_min = 0, 0  # 구간합 최대, 최소값

    for j in range(N-M+1):  #전체 순회. 이웃한 M개를 순회할 것이므로 N-(M-1)까지
        # 이웃한 M개의 값의 합
        sum_ = 0
        for k in range(j, j+M):
            sum_ += arr[k]

        # index가 0일 때로 최대, 최소값 초기화
        if j == 0:
            sum_max = sum_min = sum_
            continue

        # 최대, 최소값 갱신
        if sum_max < sum_:
            sum_max = sum_
        elif sum_min > sum_:
            sum_min = sum_

    print(f"#{i} {sum_max - sum_min}")