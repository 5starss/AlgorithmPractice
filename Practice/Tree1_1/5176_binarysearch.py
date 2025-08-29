def inorder(root):
    global cnt

    # N번노드까지 넣기
    if root <= N:
        inorder(root * 2)  # 왼쪽 끝까지 내려가기
        tree[root] = cnt  # 번호 넣기
        cnt += 1  # 번호 증가
        inorder(root * 2 + 1)  # 오른쪽으로 내려가기


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N = int(input())

    # 배열로 트리 인덱스 확인 -> levelorder
    tree = [0] * (N+1)

    # 널는 값은 1부터 시작
    cnt = 1

    # 값을 넣는 것은 inorder방식으로
    inorder(1)

    # 루트노드는 1번
    print(f"#{tc}", tree[1], tree[N//2])
