# 상하좌우로 모두 이동할 수 있는 칸 수
N = int(input())

text = [list(input()) for _ in range(N)]

# 델타 이동 사용
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 가능한 칸의 수
cnt = 0

# 4면 모서리는 모두 안되기 때문에 접근할 필요가 없음
for i in range(1, N-1):
    for j in range(1, N-1):
        for d in range(4):  # 4방향 탐색
            i += dx[d]
            j += dy[d]
            if text[i][j] != '0':  # 갈 수 없을 경우 순회 중단
                break
        else:  # 순회를 다 돌았을 경우 상하좌우 모두 접근 가능함
            cnt += 1

print(cnt)
