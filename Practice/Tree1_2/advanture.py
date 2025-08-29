'''
+1, +3, +5
3
40 4 0     #1 20
100 2 1    #2 85
3 80
20 3 1     #3 13
5 1
'''

def dfs(point, cnt=0):
    global max_

    if cnt > K:
        return
    if point in bonus:
        point = bonus[point]

    max_ = max(max_, point)

    dfs(point+1, cnt+1)
    dfs(point+3, cnt+1)
    dfs(point+5, cnt+1)


T = int(input())

for tc in range(1, T+1):
    N, K, E = map(int, input().split())

    bonus = {}

    for _ in range(E):
        bonus_point, change_point = map(int, input().split())
        bonus[bonus_point] = change_point

    max_ = 0
    point = 0

    dfs(point)

    print(f"#{tc} {max_}")

