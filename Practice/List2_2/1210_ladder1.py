def reverse(ladder, x, y):
    dx = [0, 0, -1]  # 이동 방향 설정
    dy = [-1, 1, 0]  # 왼, 오, 위 탐색

    while x > 0:  # 시작 지점까지
        for d in range(3):
            nx, ny = x + dx[d], y + dy[d]

            # 이동이 가능한 경우
            # 범위 내, 이동할 위치의 값이 1인 경우
            if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1:
                ladder[x][y] = 0  # 있던 부분 0으로 지우기
                x, y = nx, ny  # 이동

    return y  # 시작지점 리턴


if __name__ == '__main__':
    import sys

    sys.stdin = open('input.txt', 'r')

    for _ in range(10):
        tc = int(input())

        ladder = [list(map(int, input().split())) for _ in range(100)]

        # 도착 지점부터 시작
        x, y = 99, 0
        for i in range(100):
            if ladder[x][i] == 2:  # 도착 지점 찾기
                y = i
        X = reverse(ladder, x, y)  # 거꾸로 올라가기

        print(f"#{tc} {X}")



