import sys

# 재귀 호출 깊이 제한을 늘려줍니다. (N이 클 경우 필수)
sys.setrecursionlimit(10 ** 6)


sys.stdin = open("input.txt", "r")

def solve(left, right):
    # 1. 기저 조건: 더 이상 터뜨릴 풍선이 없는 경우
    if left + 1 == right:
        return 0

    # 2. 메모이제이션 확인: 이미 계산한 문제라면 저장된 값 반환
    if dp[left][right] != -1:
        return dp[left][right]

    # 3. 점화식: k를 가장 마지막에 터뜨리는 경우를 모두 시도
    max_score = 0
    for k in range(left + 1, right):
        # 재귀 호출로 하위 문제의 정답을 가져옴
        score = solve(left, k) + solve(k, right) + (A[left] * A[right])
        max_score = max(max_score, score)

    # 4. 결과 저장 및 반환
    dp[left][right] = max_score
    return max_score


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    A = [1] + arr + [1]
    n_padded = N + 2

    # 메모이제이션 테이블을 -1로 초기화
    dp = [[-1] * n_padded for _ in range(n_padded)]

    # 가장 큰 문제인 solve(0, n_padded - 1)를 호출할 필요는 없습니다.
    # 왜냐하면 최종 정답은 마지막 풍선 규칙을 따로 적용해야 하기 때문입니다.
    # 각 하위 문제들을 먼저 풀어 dp 테이블을 채웁니다.

    # 최종 정답 계산 (바텀업 방식과 동일)
    ans = 0
    for k in range(1, N + 1):
        # solve(0, k)와 solve(k, n_padded - 1)를 호출하면
        # 필요한 모든 하위 문제들이 재귀적으로 계산되고 dp 테이블에 저장됩니다.
        total_score = solve(0, k) + solve(k, n_padded - 1) + A[k]
        ans = max(ans, total_score)

    print(f"#{tc} {ans}")