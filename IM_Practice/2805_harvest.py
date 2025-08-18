import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(arr)
    i = 1
    ans = sum(arr[N//2])
    while i <= (N//2):
        print(ans)
        ans += sum(arr[N//2+i][i:-i])
        print(ans)
        ans += sum(arr[N // 2 - i][i:-i])
        i += 1

    print(f"#{tc} {ans}")
