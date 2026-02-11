def printer(want):
    cnt = 1

    while q:
        if len(q) == 1:
            return cnt

        current_i, current_v = arr.pop(0)
        current = q.pop(0)

        if current_v >= max(q):
            if current_i == want:
                break
            cnt += 1
        else:
            arr.append((current_i,current_v))
            q.append(current)

    return cnt


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    arr = []
    for i, v in enumerate(q):
        arr.append((i, v))
    print(printer(M))