def preorder(start):
    if start:
        print(start, end=' ')  # 내려가면서 출력
        preorder(adj_list[start][0])  # 왼쪽 자식 노드부터 확인
        preorder(adj_list[start][1])  # 왼쪽 자식 노드 확인이 끝나면 오른쪽 자식 노드 확인


def preorder2(start):
    if start:
        print(start, end=' ')
        preorder2(left[start])
        preorder2(right[start])


def inorder(start):
    if start:
        inorder(adj_list[start][0])  # 일단 왼쪽 끝으로 내려간 후
        print(start, end=' ')  # 출력
        inorder(adj_list[start][1])  # 왼쪽 노드, 부모 노드 출력 후 오른쪽 노드 출력


def inorder2(start):
    if start:
        inorder2(left[start])
        print(start, end=' ')
        inorder2(right[start])


def postorder(start):
    if start:
        postorder(adj_list[start][0])
        postorder(adj_list[start][1])
        # 왼쪽노드, 오른쪽노드 출력 후 부모노드 출력
        print(start, end=' ')


def postorder2(start):
    if start:
        postorder2(left[start])
        postorder2(right[start])
        print(start, end=' ')


# BFS의 느낌으로 출력
def levelorder(start):
    q = [start]  # 큐 생성

    # 위에서부터 아래로 순서대로 출력
    while q:
        v = q.pop(0)
        print(v, end=' ')  # 출력

        for i in adj_list[v]:  # 인접한 노?드 확인
            if i:
                q.append(i)  # 인접한 노드를 큐에 추가


def levelorder2(start):
    q = [start]

    while q:
        v = q.pop(0)
        print(v, end=' ')

        if left[v]:
            q.append(left[v])
        if right[v]:
            q.append(right[v])

V = 13
E = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

root = 0

# -------------------------------------
adj_list = [[0, 0] for _ in range(max(E)+1)]  # 인접 리스트로 저장. 인덱스가 부모노드, 해당 리스트가 자식노드
parent = [0] * (V+1)  # 부모노드 확인. 루트 확인용

for i in range(V-1):  # 인접 리스트 만들기
    v1, v2 = E[i*2], E[i*2+1]
    if not adj_list[v1][0]:  # 왼쪽 자식부터 추가
        adj_list[v1][0] = v2
    else:  # 왼쪽 자식이 있다면 오른쪽 자식으로 추가
        adj_list[v1][1] = v2
    parent[v2] = v1  # 부모노드 저장

# 루트노드 찾기
for i in range(1, V+1):
    if not parent[i]:
        root = i

print("preorder:", end=' ')
preorder(root)
print()

print("inorder:", end=' ')
inorder(root)
print()

print("postorder:", end=' ')
postorder(root)
print()

print("levelorder:", end=' ')
levelorder(root)
print()

print("--------------------------------------")
# --------------------------------------
parent2 = [0] * (V+1)  # 부모노드 확인용
left = [0] * (V+1)  # 왼쪽 자식노드. 인덱스는 자기 자신, 값은 왼쪽 자식노드
right = [0] * (V+1)  # 오른쪽 자식노드. 인덱스는 자기 자신, 값은 오른쪽 자식노드

for i in range(V-1):  # 부모노드, 자식노드 추가
    v1, v2 = E[i * 2], E[i * 2 + 1]
    if not left[v1]:
        left[v1] = v2
    else:
        right[v1] = v2

    parent2[v2] = v1

# 루트노드 찾기
for i in range(1, V+1):
    if not parent2[i]:
        root = i

print("preorder:", end=' ')
preorder2(root)
print()

print("inorder:", end=' ')
inorder2(root)
print()

print("postorder:", end=' ')
postorder2(root)
print()

print("levelorder:", end=' ')
levelorder2(root)
print()