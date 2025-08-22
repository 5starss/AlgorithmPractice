import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]  # N x N 빈 행렬 만들기

    # 델타 이동 이용
    dx = [0, 1, 0, -1]  # 이동할 값
    dy = [1, 0, -1, 0]  # 우측으로 이동, 아래로 이동, 좌측으로 이동, 위로 이동

    # 시작 좌표는 0,0. 값은 1부터 시작
    num = 1
    x, y = 0, 0
    snail[x][y] = num
    while num < N**2:  # N=3인 경우 9까지, 4인경우 16까지
        for i in range(4):  # 빙글빙글 돌기
            # 조건 찾기 어려우면 일단 while True 후 조건이 맞지 않는 경우 break
            # 반복 조건 - 행렬 벗어나지 않기, 값이 없는 쪽으로 가기
            while 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and snail[x + dx[i]][y + dy[i]] == 0:
                # 이동
                x += dx[i]
                y += dy[i]
                # 숫자 증가
                num += 1
                snail[x][y] = num

    print(f"#{tc}")
    for i in range(N):
        print(' '.join(map(str, snail[i])))  # 행마다 출력
