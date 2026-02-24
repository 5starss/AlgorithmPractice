N = int(input())
num = N
result = [0 for _ in range(num+1)]

result[1] = 1
if N > 1:
    result[2] = 3
    for i in range(3, num+1):
        result[i] = result[i-1] + 2*result[i-2]

print(result[num] % 10007)