from collections import deque

# 스택을 이용하여 거리 구하기, visited 미사용
def DFS_stack(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 0  # 거리
    stack = [(cnt, x, y)]  # (거리, 좌표)

    while stack:
        cnt, current_x, current_y = stack.pop()  # 이동 거리, 현재 좌표

        arr[current_x][current_y] = 1  # 방문 했다는 것을 표시

        for d in range(4):  # 델타이동 탐색
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:  # 행렬 가장자리 제한
                if arr[nx][ny] == 0:  # 길인 경우
                    stack.append((cnt+1, nx, ny))  # 스택에 추가, 이동 거리+1
                elif arr[nx][ny] == 3:  # 도착지점이 보이는 경우
                    return cnt  # 이동 거리 반환

    return 0  # 도착지점에 도착하지 못한 경우

# 재귀를 이용한 DFS을 이용한 방법
def DFS_recursive(x, y, cnt=0):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    arr[x][y] = 1  # 방문 표시

    for d in range(4):  # 델타 이동 탐색
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:  # 행렬 가장자리 제한
            if arr[nx][ny] == 0:  # 길인 경우
                result = DFS_recursive(nx, ny, cnt + 1)  # 탐색
                if result:  # 거리를 리턴한 경우, 0이 아닌경우
                    return result  # 계속 그 거리를 리턴

            elif arr[nx][ny] == 3:  # 도착지점에 도착한 경우
                return cnt  # 이동한 거리를 반환

    return 0  # 도착지점에 도착하지 못한 경우 0 반환


# 큐를 이용한 방법, visited 미사용
def BFS(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 0  # 이동거리 저장
    q = [(cnt, x, y)]  # 이동거리, 좌표

    while q:
        cnt, current_x, current_y = q.pop(0)

        arr[current_x][current_y] = 1  # 방문했다는 것을 표시

        for d in range(4):  # 델타 이동
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:  # 제한 범위 설정
                if arr[nx][ny] == 0:  # 길인 경우
                    q.append((cnt+1, nx, ny))  # 큐에 저장
                elif arr[nx][ny] == 3:  # 도착 지점에 도착
                    return cnt  # 이동 거리 반환

    return 0  # 도착 지점에 도착하지 못한 경우


# deque 사용, visited 미사용
def BFS_deque(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 0

    # q = deque([(cnt, x, y)])
    q = deque()
    q.append((cnt, x, y))  # 이동 거리, 좌표

    while q:
        cnt, current_x, current_y = q.popleft()

        for d in range(4):  # 델타 이동
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:  # 제한 범위 설정
                if arr[nx][ny] == 0:  # 길인 경우
                    arr[nx][ny] = 1  # 방문 예정이라는 것을 표시
                    q.append((cnt+1, nx, ny))  # 큐에 넣기
                elif arr[nx][ny] == 3:  # 도착 지점에 도착
                    return cnt  # 이동 거리 반환

    return 0  # 도착 지점에 도착하지 못한 경우


# 큐 이용, visited에 이동 거리 저장
def BFS_visited(x, y):
    # 전체 행렬 크기만큼 이동거리를 저장할 행렬 초기화
    # 이를 통해 방문여부도 확인 가능
    visited = [[0 for _ in range(N)] for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([(x, y)])  # 큐에 초기값 저장

    while q:
        current_x, current_y = q.popleft()  # 현재 좌표

        for d in range(4):  # 델타 이동
            nx = current_x + dx[d]
            ny = current_y + dy[d]

            # 행렬에 벗어나지 않게끔 설정 + 방문 여부 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == 0:  # 인접 노드인 경우
                    q.append((nx, ny))  # 큐에 넣기
                    visited[nx][ny] = visited[current_x][current_y] + 1  # 이동 거리 저장
                elif arr[nx][ny] == 3:  # 도착 지점에 도착
                    return visited[current_x][current_y]  # 이동 거리 반환

    return 0  # 도착 지점에 도착하지 못한 경우


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N = int(input())  # 미로 크기
    arr = [list(map(int, input())) for _ in range(N)]  # 미로

    # 출발 지점 찾기
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 출발 지점
                x, y = i, j

    # ans = DFS_stack(x, y)

    # ans = DFS_recursive(x, y)

    # ans = BFS(x, y)

    # ans = BFS_deque(x, y)

    ans = BFS_visited(x, y)

    print(f"#{tc} {ans}")
