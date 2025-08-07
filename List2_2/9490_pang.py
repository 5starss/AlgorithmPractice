import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N x M 행렬
    balloon = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]  # 이동할 값
    dy = [1, 0, -1, 0]

    max_sum = 0  # 최대 값
    # 전체 순회
    for i in range(N):
        for j in range(M):
            # 자기 자신 추가
            sum_ = balloon[i][j]
            # 확인할 거리 확인
            power = balloon[i][j]
            for d in range(4):  # 상하좌우 확인
                for p in range(1, power+1):  # 거리 확인
                    nx = i + dx[d] * p
                    ny = j + dy[d] * p

                    if 0 <= nx < N and 0 <= ny < M:  # 전체 범위 넘어가지 않기
                        sum_ += balloon[nx][ny]
            max_sum = max(max_sum, sum_)  # 최대값 갱신

    print(f"#{tc} {max_sum}")
