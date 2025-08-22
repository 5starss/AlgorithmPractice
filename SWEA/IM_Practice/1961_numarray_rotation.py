def rotate(arr):
    N = len(arr)
    arr2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr2[j][N-i-1] = arr[i][j]
    return arr2
'''
[0][0] -> [0][2]
[0][1] -> [1][2]
[0][2] -> [2][2]
[1][0] -> [0][1]
[1][1] -> [1][1]
[1][2] -> [2][1]
[2][0] -> [0][0]
[2][1] -> [1][0]
[2][2] -> [2][0]
'''

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    print(f"#{tc}")
    for i in range(N):
        arr = rotate(arr)
        for _ in range(3):
            print(''.join(map(str, arr[i])), end=' ')
            arr = rotate(arr)
        print()
