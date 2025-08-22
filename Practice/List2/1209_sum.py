import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_r, max_c, max_d = 0, 0, 0  # 행, 열, 대각선의 합 중 최대값

    # 행의 합 중 최대값 찾기
    for r in range(100):
        sum_r = 0  # 각 행의 합
        for c in range(100):
            sum_r += arr[r][c]
        if max_r < sum_r:  # 최대값 갱신. max()로 대체 가능.
            max_r = sum_r

    # 열의 합 중 최대값 찾기
    for c in range(100):
        sum_c = 0  # 각 열의 합
        for r in range(100):
            sum_c += arr[r][c]
        if max_c < sum_c:  # 최대값 갱신
            max_c = sum_c

    # 대각선의 합 중 최대값 찾기
    # 대각선 1
    sum_d = 0
    for i in range(100):
        sum_d += arr[i][i]
    if max_d < sum_d:
        max_d = sum_d

    sum_d = 0
    for i in range(100):
        sum_d += arr[i][99-i]
    if max_d < sum_d:
        max_d = sum_d

    print(f"#{tc} {max(max_r, max_c, max_d)}")

'''내장함수 + 리스트컴프리헨션 사용
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합 중 최대값 찾기
    max_r = max([sum(r) for r in arr])
    # 열의 합 중 최대값 찾기
    max_c = max([sum(c) for c in zip(*arr)])  # zip은 같은index(열)끼리 묶어서 tuple로 저장
    # 대각선의 합
    sum_d1 = sum([arr[d][d] for d in range(100)])
    sum_d2 = sum([arr[d][99-d] for d in range(100)])

    print(f"#{tc} {max(max_r, max_c, sum_d1, sum_d2)}")
'''