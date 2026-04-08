import sys
input = sys.stdin.readline

def recur(cnt=0):
    if cnt == M:
        tmp = answer[0]
        for i in range(1, M):
            tmp *= 10000
            tmp += answer[i]

        if tmp not in set_visited:  # set 으로 찾는게 O(1)
            set_.append(answer[:])
            set_visited.add(tmp)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            answer.append(arr[i])
            recur(cnt+1)
            visited[i] = 0
            answer.pop()

    return

N, M = map(int, input().split())
arr = sorted(list(map(int,input().split())))
visited = [0] * N
answer = []
set_visited = set() # set 으로 찾는게 O(1)
set_ = []

recur()


for i in set_:
    print(*i)