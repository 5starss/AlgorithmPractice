import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    set_1 = set(map(int, input().split()))
    set_2 = set(range(1, N+1))

    ans = sorted(list(set_2 - set_1))

    print(f"#{tc}", *ans)
