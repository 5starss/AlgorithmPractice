def preorder_count(start):  # preorder
    global cnt
    if start:
        cnt += 1  # 개수 추가
        preorder_count(adj_list[start][0])
        preorder_count(adj_list[start][1])


def inorder_count(start):
    global cnt
    if start:
        inorder_count(adj_list[start][0])
        cnt += 1
        inorder_count(adj_list[start][1])


def postorder_count(start):
    global cnt
    if start:
        postorder_count(adj_list[start][0])
        postorder_count(adj_list[start][1])
        cnt += 1


def levelorder_count(start):
    global cnt
    q = [start]

    # 위에서부터 아래로 순서대로 출력
    while q:
        v = q.pop(0)
        cnt += 1

        for i in adj_list[v]:
            if i:
                q.append(i)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    E, N = map(int, input().split())  # E: 간선 수, N: 서브트리의 루트
    arr = list(map(int, input().split()))

    # 인접리스트
    adj_list = [[0, 0] for _ in range(max(arr)+1)]

    # 인접 리스트 만들기
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]
        if not adj_list[n1][0]:
            adj_list[n1][0] = n2
        else:
            adj_list[n1][1] = n2

    # 서브 트리 내 총 노드
    cnt = 0

    # preorder방식으로 카운트
    # preorder_count(N)

    # inorder방식으로 카운트
    # inorder_count(N)

    # postorder방식으로 카운트
    # postorder_count(N)

    # levelorder방식으로 카운트
    # levelorder_count(N)

    print(f"#{tc} {cnt}")

