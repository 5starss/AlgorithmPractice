def preorder_count(start):  # preorder
    global cnt
    cnt += 1  # 개수 추가
    for i in adj_list[start]:
        preorder_count(i)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    E, N = map(int, input().split())  # E: 간선 수, N: 서브트리의 루트
    arr = list(map(int, input().split()))

    # 인접리스트
    adj_list = [[] for _ in range(max(arr)+1)]

    # 인접 리스트 만들기
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]
        adj_list[n1].append(n2)

    # 서브 트리 내 총 노드
    cnt = 0

    # preorder방식으로 카운트
    preorder_count(N)

    print(f"#{tc} {cnt}")

