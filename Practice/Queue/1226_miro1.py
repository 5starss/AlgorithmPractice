from collections import deque

# 스택을 이용
def DFS_stack(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    stack = [(x, y)]  # 시작 지점

    while stack:
        current_x, current_y = stack.pop()  # 현재 좌표

        arr[current_x][current_y] = 1  # 방문 여부 저장 -> 벽으로 만듦

        for d in range(4):  # 델타 이동
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            # 미로의 가장자리에 1로 벽을 만들어놔서 행렬을 벗어날 일이 없음
            if arr[nx][ny] == 0:  # 길인 경우
                stack.append((nx, ny))  # 스택에 추가
            elif arr[nx][ny] == 3:  # 도착 지점에 도착
                return 1  # 1 리턴

    return 0  # 도착 지점에 도착하지 못한 경우


# 재귀 함수 이용
def DFS_recursive(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    if arr[x][y] == 3:  # 도착지점에 도착한 경우
        return 1

    arr[x][y] = 1  # 방문 여부 저장

    for d in range(4):  # 델타 이동
        nx = x + dx[d]
        ny = y + dy[d]

        # 미로의 가장자리에 1로 벽을 만들어놔서 행렬을 벗어날 일이 없음
        if arr[nx][ny] in (0, 3):  # 이동 가능한 경우
            if DFS_recursive(nx, ny):  # 재귀함수의 리턴이 1인 경우 = 도착지점에 도착한 경우
                return 1  # 계속 1을 리턴

    return 0  # 도착지점에 도착하지 못한 경우


# 큐를 이용
def BFS(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = [(x, y)]  # 시작 지점

    while q:
        current_x, current_y = q.pop(0)

        arr[current_x][current_y] = 1  # 방문 여부 저장

        for d in range(4):  # 델타 이동
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            # 미로의 가장자리에 1로 벽을 만들어놔서 행렬을 벗어날 일이 없음
            if arr[nx][ny] == 0:  # 길인 경우
                q.append((nx, ny))  # 큐에 저장
            elif arr[nx][ny] == 3:  # 도착 지점인 경우
                return 1  # 1 리턴

    return 0  # 도착 지점에 도착하지 못한 경우우

def BFS_deque(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([(x, y)])  # 시작 지점

    while q:
        current_x, current_y = q.popleft()  # 현재 좌표

        for d in range(4):  # 델타 이동
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            # 미로의 가장자리에 1로 벽을 만들어놔서 행렬을 벗어날 일이 없음
            if arr[nx][ny] == 0:  # 길인 경우
                arr[nx][ny] = 1  # 방문 예정 저장
                q.append((nx, ny))  # 큐에 넣기
            elif arr[nx][ny] == 3:  # 도착 지점이 보이는 경우
                return 1  # 1 반환

    return 0  # 도착 지점에 도착하지 못한 경우


# visited를 사용하여 방문 여부를 저장하는 경우
def BFS_visited(x, y):
    visited = [[False for _ in range(16)] for _ in range(16)]  # 미로 크기만큼 방문 여부 확인용 행렬 초기화

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([(x, y)])  # 시작 지점

    while q:
        current_x, current_y = q.popleft()  # 현재 좌표

        if arr[current_x][current_y] == 3:  # 도착 지점에 도착한 경우
            return 1  # 1 반환

        for d in range(4):  # 델타 이동
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            if arr[nx][ny] in (0, 3) and not visited[nx][ny]:  # 이동 가능한 경우 + 방문하지 않은 경우
                visited[nx][ny] = True  # 방문 여부 저장
                q.append((nx, ny))  # 큐에 저장

    return 0  # 도착 지점에 도착하지 못한경우


import sys

sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    # ans = DFS_stack(1, 1)
    # ans = DFS_recursive(1, 1)
    # ans = BFS(1, 1)
    # ans = BFS_deque(1, 1)
    ans = BFS_visited(1, 1)

    print(f"#{tc} {ans}")
