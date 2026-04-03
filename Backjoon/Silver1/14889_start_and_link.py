def check(team1, team2):
    sum_team1, sum_team2 = 0, 0
    for i in range(len(team1)):
        for j in range(len(team1)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)


def recur(cnt):
    if cnt == N+1:
        return

    if len(team1) == N // 2:
        team2 = list(set_ - set(team1))
        ans.append(check(team1, team2))
        return
    for i in range(cnt, N):
        team1.append(i)
        recur(i+1)
        team1.pop()

    return

N = int(input())
set_ = set([i for i in range(N)])
team1 = []
ans = []

arr = [list(map(int, input().split())) for _ in range(N)]

recur(0)

print(min(ans))


"""  빠른 답안
import sys

input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

s_team = [None] * (N // 2)
visited = [False] * N

# 0번은 무조건 스타트팀
visited[0] = True
s_team[0] = 0

answer = float("Inf")
pair = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        pair[i][j] = board[i][j] + board[j][i]


def get_ability(team: list[int]) -> int:
    ability = 0

    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            a, b = team[i], team[j]
            ability += pair[a][b]

    return ability


def backtrack(k, start):
    global answer

    if k == N // 2:
        l_team = [i for i in range(N) if not visited[i]]
        diff = abs(get_ability(s_team) - get_ability(l_team))
        answer = min(answer, diff)
        return
    for i in range(start, N):
        if not visited[i]:
            s_team[k] = i
            visited[i] = True
            backtrack(k + 1, i + 1)
            visited[i] = False


backtrack(1, 1)
print(answer)
"""