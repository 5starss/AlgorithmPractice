# 피해구역 수
N = int(input())

text = [input() for _ in range(N)]

# #개수
cnt = 0

# 전체 순회
for i in range(N):
    for j in range(N):
        if text[i][j] == '#':  # #찾기
            cnt += 1

print(cnt)