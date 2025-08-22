import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0  # 가장 많이 파리를 죽이는 경우
    for r in range(N-M+1):  # 전체 순회
        for c in range(N-M+1):
            sum_kill = 0  # 내려쳤을 때 죽는 파리 합
            for i in range(M):
                for j in range(M):
                    sum_kill += arr[r+i][c+j]
            if max_kill < sum_kill:  # 최대값 갱신. max()로 대체 가능.
                max_kill = sum_kill

    print(f"#{tc} {max_kill}")