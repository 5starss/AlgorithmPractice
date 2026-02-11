import sys
input = sys.stdin.readline  # 시간 단축

N, M = map(int, input().split())
dic = dict()
for _ in range(N):
    url, password = input().split()
    dic[url] = password

for _ in range(M):
    print(dic[input().strip()])