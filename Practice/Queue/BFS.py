'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

# 인접 리스트를 처리
def bfs1(s, V):  # 시작정점 s, 마지막 정점 V
    visited = [0] * (V+1)   # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:        # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)    # 디큐
        print(t)        # 방문한 정점에서 할일
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w]==0:
                q.append(w)     # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1

# 인접 행렬을 처리
def bfs2(s, V):  # 시작정점 s, 마지막 정점 V
    visited = [0] * (V+1)   # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:        # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)    # 디큐
        print(t)        # 방문한 정점에서 할일
        for w in range(1, V+1):
            if adj_matrix[t][w] == 1 and visited[w] == 0:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
                q.append(w)     # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1


V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접 리스트
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 양방향

bfs1(1, 7)

print('--------------------------')

# 인접 행렬
adj_matrix = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1    # 양방향

bfs2(1, 7)

