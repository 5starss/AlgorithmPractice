import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    coloring_area = [[0] * 10 for _ in range(10)]  # 색을 입힐 2차원 배열

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())  # 색을 입힐 범위
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if coloring_area[r][c] != color:  # 색이 다를 경우 색을 입힘. 빨+빨, 파+파 방지
                    coloring_area[r][c] += color

    cnt = 0
    for i in range(10):  # 입혀진 색 확인
        for j in range(10):
            if coloring_area[i][j] == 3:  # 3일경우 보라
                cnt += 1
    print(f"#{tc} {cnt}")
