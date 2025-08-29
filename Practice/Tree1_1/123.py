# 입력값 받기
T = int(input())
for tc in range(1, T+1):
    E, node = map(int, input().split()) # 간선의 개수 E와 루트 node
    arr = list(map(int, input().split()))
    # E: 간선의 개수 -> 인덱스를 맞추기 위해서는 노드 수 +1 -> 노드 수는 간선의 개수 + 1
    parent = [0] * (E + 2)
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    # 부모, 왼손, 오른손에 간선에 따라 값 할당
    for i in range(E):
        R, r = arr[2 * i], arr[2 * i + 1]
        if left[R] == 0:
            left[R] = r
        else:
            right[R] = r
        parent[r] = R
    # root = 0
    # for i in range(1, E + 2):
    #     if parent[i] == 0:
    #         root = i
    # 루트를 중심으로 노드의 수 구하기 : 전위 순회 사용
    cnt = 0 # 노드 수 초기화
    def num_node(node):
        global cnt
        if node:
            cnt += 1
            num_node(left[node])
            num_node(right[node])

    num_node(node) # 함수 호출
    print(f'#{tc} {cnt}')