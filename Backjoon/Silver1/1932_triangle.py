n = int(input())
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(n-1, 0, -1):
    for j in range(len(arr[i])-1):
        arr[i-1][j] += max(arr[i][j:j+2])

print(arr[0][0])