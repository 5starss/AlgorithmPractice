N = int(input())

arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(N-1):
    tmp = [0] * 10
    for i in range(10):
        if i == 0:
            tmp[0] = arr[1]
        elif i == 9:
            tmp[9] = arr[8]
        else:
            tmp[i] = arr[i-1] + arr[i+1]
    arr = tmp

print(sum(arr) % 1000000000)