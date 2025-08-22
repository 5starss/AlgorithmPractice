# 스택으로 풀기. visited는 방문 여부만
def DFS(start, end):
    visited = [0] * (V + 1)  # 방문 여부만 확인. 0, 1
    cnt = 0  # 이동 거리 저장
    stack = [(cnt, start)]  # 이동 거리, 노드

    while stack:
        cnt, current = stack.pop()  # 이동 거리, 현재 노드

        if current == end:  # 도착지점에 도착
            return cnt  # 이동 거리 반환

        # 순서에 대한 추가요건이 없기 때문에 앞에서부터 넣어도 상관 없음
        # 만약 작은 순서부터 방문한다는 조건이 있으면 range(V, 0, -1)로 설정
        for next in range(1, V + 1):
            # 인접한 노드인 경우, 방문한 적 없는 노드인 경우
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                stack.append((cnt + 1, next))  # 이동거리+1, 인접노드 추가
                visited[next] = 1  # 방문 여부 확인

    return 0


# 스택으로 풀어보기, visited에 이동 거리 저장
def DFS_visited(start, end):
    visited = [0] * (V+1)  # 방문 여부 확인, 출발지점으로부터의 거리

    stack = [start]  # 첫 시작

    while stack:
        current = stack.pop()

        if current == end:  # 도착 지점에 도착
            return visited[end]  # 거리 반환

        for next in range(1, V+1):
            # 인접한 노드인 경우, 방문한 적 없는 노드인 경우
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                stack.append(next)
                visited[next] = visited[current] + 1  # 이동한 거리를 visited에 저장 -> 방문여부도 확인 가능

    return 0

# 재귀를 이용해서 푸는 방법. 방문여부는 재귀 함수 밖에 설정
def DFS_recursive(start, end, cnt=0):
    if start == end:  # 도착 지점에 도착
        return cnt  # 이동 거리를 반환

    visited[start] = 1

    # 순서에 대한 추가요건이 없기 때문에 앞에서부터 넣어도 상관 없음
    # 해당 코드는 뒤에서부터 넣은 방법
    for next in range(V, 0, -1):
        # 인접한 노드인 경우, 방문한 적 없는 경우
        if adj_matrix[start][next] == 1 and visited[next] == 0:
            result = DFS_recursive(next, end, cnt+1)  # 재귀
            if result:  # 이동 거리를 반환한 경우(0이 아닌경우)
                return result  # 계속 이동 거리를 반환

    return 0  # 도착 지점에 도착하지 못한 경우


# 큐로 풀어보기. visited는 방문 여부만 저장
def BFS(start, end):
    visited = [0] * (V+1)  # 방문 여부 확인용
    cnt = 0  # 이동 거리 저장
    q = [(cnt, start)]  # 이동 거리, 노드

    while q:
        cnt, current = q.pop(0)  # 이동 거리, 현재 노드

        if current == end:  # 도착 지점에 도착
            return cnt  # 이동 거리 반환

        # 큐는 먼저 넣은 것이 먼저 뽑히므로 순서대로 넣는다.
        for next in range(1, V+1):
            # 인접한 노드인 경우, 방문한 적 없는 노드인 경우
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                q.append((cnt+1, next))  # 이동거리+1, 인접노드 추가
                visited[next] = 1  # 방문 여부 확인

    return 0


# 큐로 풀어보기. visited에 이동 거리 저장
def BFS_visited(start, end):
    visited = [0] * (V+1)  # 방문여부 확인, 이동거리 저장

    q = [start]  # 노드

    while q:
        current = q.pop(0)  # 현재 노드

        if current == end:  # 도착 지점에 도착
            return visited[end]  # 이동 거리 반환

        for next in range(1, V+1):
            if adj_matrix[current][next] == 1 and visited[next] == 0:
                q.append(next)
                visited[next] = visited[current] + 1  # 이동 거리 저장

    return 0


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    V, E = map(int, input().split())  # 정점 수, 간선 수
    adj_matrix = [[0] * (V+1) for _ in range(V+1)]  # 인접 행렬

    # 간선 확인
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_matrix[v1][v2] = 1
        adj_matrix[v2][v1] = 1

    S, G = map(int, input().split())  # 출발지점, 도착지점

    # ans = DFS(S, G)
    # ans = DFS_visited(S. G)
    visited = [0] * (V + 1)
    ans = DFS_recursive(S, G)
    # ans = BFS(S, G)
    # ans = BFS_visited(S, G)

    print(f"#{tc} {ans}")
