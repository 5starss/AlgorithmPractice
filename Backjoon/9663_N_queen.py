def check(c, r):
    for now in range(r): # 상위 줄 체크
        if visited[now] == c or r - now == abs(visited[r] - visited[now]):  # 같은 줄에 퀸이 있는지 확인 + 대각선에 있는지 확인(대각선 = (열차이 == 행차이)
            return False

    return True


def queen(r=0):
    global ans
    if r == N:  # 끝까지 왔다면 완성
        ans += 1
        return

    for c in range(N):
        visited[r] = c
        if check(c, r):
            queen(r+1)


N = int(input())
visited = [-1] * N
ans = 0

queen()
print(ans)
