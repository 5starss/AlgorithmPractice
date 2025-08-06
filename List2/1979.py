import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 행 검색
    ans = 0  # 들어갈 수 있는 자리의 개수
    for i in range(N):
        cnt = 0  # 1의 개수
        for j in range(N):
            if puzzle[i][j] == 1:  # 행 검색
                cnt += 1
            elif puzzle[i][j] == 0:  # cnt를 확인하는 구간
                if cnt == K:  # 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리
                    ans += 1
                cnt = 0
        if cnt == K:  # 마지막에도 확인
            ans += 1

    # 열 검색
    for i in range(N):
        cnt = 0  # 1의 개수
        for j in range(N):
            if puzzle[j][i] == 1:  # 열 검색
                cnt += 1
            elif puzzle[j][i] == 0:  # cnt를 확인하는 구간
                if cnt == K:  # 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리
                    ans += 1
                cnt = 0
        if cnt == K:  # 마지막에도 확인
            ans += 1

    print(f"#{tc} {ans}")