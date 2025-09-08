def synergy(path):
    path1 = path
    path2 = list(set(range(N)) - set(path))
    # print(path1, path2)

    synergy1 = 0
    synergy2 = 0
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            synergy1 += adj_mat[path1[i]][path1[j]]
            synergy1 += adj_mat[path1[j]][path1[i]]
            synergy2 += adj_mat[path2[i]][path2[j]]
            synergy2 += adj_mat[path2[j]][path2[i]]

    return abs(synergy1-synergy2)


def combination(cnt, path):
    global min_gap

    if cnt == N:
        if len(path) == N//2 and path[0] == 0:
            # combi_list.append(path)
            min_gap = min(min_gap, synergy(path))
        return

    combination(cnt+1, path+[cnt])
    combination(cnt+1, path)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    adj_mat = [list(map(int, input().split())) for _ in range(N)]

    min_gap = float('inf')

    combi_list = []
    combination(0, [])

    print(f"#{tc} {min_gap}")

