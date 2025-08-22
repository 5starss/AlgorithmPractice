
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = N//10
    result = [0 for _ in range(num+1)]

    result[1] = 1
    result[2] = 3
    for i in range(3, num+1):
        result[i] = result[i-1] + 2*result[i-2]

    print(f"#{tc} {result[num]}")