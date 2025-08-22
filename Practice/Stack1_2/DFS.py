"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# 1. 그래프 정보 받기
# V: 노드의 개수 E: 간선 개수
V, E = map(int, input().split())

# 간선의 정보를 담은 리스트
data = list(map(int, input().split()))

# 2. 인접 행렬 초기화
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 3. 인접 행렬에 간선정보 기록
# 입력 받은 data 리스트를 순회 하며, 간선 정보를 인접 행렬에 기록
# 데이터는 시작과 끝으로 쌍 지어있다. (시작 노드, 끝 노드)
# 그래프는 방향성을 가질 수 있다.
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    # 무방향 그래프이다. 양쪽에 모두 기록한다.
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

"""
"내가 다시 돌아올 곳을 저장"
완전 탐색인데, 스택을 활용해서, 내가 왔던 길(정점)로 돌아가서, 다른 방향의 정점을 반복 탐색
모든 정점(길)을 다 완전 탐색하는 것이 최종 목표
- 스택의 후입선출을 활용한다.
- 파이썬에서는 함수 호출이 Call Stack에 들어가는데, 마찬가지로 Stack을 활용한다.
- 대부분 DFS는 재귀함수를 활용하는 편이다.
"""


def DFS_stack(start):
    stack = [start]
    visited = [0] * (V + 1)

    while stack:
        current = stack.pop()

        if visited[current] == 0:
            visited[current] = 1
            print(current, end='')

            for next in range(V+1, 0, -1):
                if adj_matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)


DFS_stack(1)

visited = [0] * (V + 1)


def DFS_recursive(start):
    visited[start] = 1
    print(start, end=' ')

    for next in range(1, V + 1):
        if adj_matrix[start][next] == 1 and visited[next] == 0:
            DFS_recursive(next)


DFS_recursive(1)
