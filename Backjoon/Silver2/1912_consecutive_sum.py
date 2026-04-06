N = int(input())
arr = list(map(int, input().split()))

for i in range(N-2, -1, -1):
    a, b = arr[i], arr[i+1]
    if a + b > a:
        arr[i] = a + b

print(max(arr))
