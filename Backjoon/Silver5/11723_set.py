import sys
input = sys.stdin.readline  # 그냥 input 써도 가능함

S = set()
M = int(input())
for _ in range(M):
    parts = input().split()
    calc = parts[0]

    if calc in ("all", "empty"):
        num = None
    else:
        num = int(parts[1])

    if calc == 'add':
        S.add(num)
    elif calc == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif calc == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif calc == 'remove':
        if num in S:
            S.remove(num)
    elif calc == 'all':
        S = {i for i in range(1, 21)}
    else:
        S = set()
