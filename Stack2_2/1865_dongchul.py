def f(i, s):  # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global max_v

    if max_v >= s:  # 중간 합계가 최대합보다 작으면
        return

    if i == N:
        max_v = max(s, max_v)
        return

    for col in range(N):
        if not visited_cols[col]:
            visited_cols[col] = True
            f(i + 1, s * (arr[i][col]/100.0))  # i+1자리 결정
            visited_cols[col] = False # 방문 해제 (선택 취소 - 백트래킹)

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 배열의 크기 N x N
    arr = [list(map(int, input().split())) for _ in range(N)]

    # p = [i for i in range(N)]  # P[i] : i에서 고른 열 번호
    visited_cols = [False] * N
    max_v = 0.0
    f(0, 1.0)
    print(f"#{tc} {max_v * 100:.6f}")

# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     # 입력값을 미리 100으로 나눈 확률(float)로 저장
#     arr = [list(map(lambda x: int(x) / 100.0, input().split())) for _ in range(N)]
#
#     # dp[mask]: mask에 표시된 열들을 사용했을 때의 최대 곱
#     # -1.0으로 초기화하여 '계산 안 된 상태'와 '계산 결과가 0인 상태'를 구분
#     dp = [-1.0] * (1 << N)
#
#     # 기본 상태: 아무것도 선택하지 않았을 때(0개의 행, 0개의 열)의 곱은 1
#     dp[0] = 1.0
#
#     # mask: 1부터 (2^N - 1)까지 모든 열의 조합을 순회
#     for mask in range(1, 1 << N):
#
#         # 현재 행의 인덱스 계산
#         # mask에 켜진 비트의 수가 사용한 행/열의 개수. -1을 하면 현재 행 인덱스가 됨
#         row_idx = bin(mask).count('1') - 1
#
#         # 모든 열 j에 대하여, 이 j가 현재 행(row_idx)에 할당될 후보라고 가정
#         for j in range(N):
#             # j번 열이 현재 mask에 포함되어 있는지 확인 (j번 비트가 켜져 있는지)
#             if (mask & (1 << j)):
#
#                 # 이전 상태의 마스크 (현재 mask에서 j번 비트를 끈 상태)
#                 prev_mask = mask ^ (1 << j)
#
#                 # 이전 상태가 유효한 경우에만(즉, 계산된 적이 있는 경우) 계산 진행
#                 if dp[prev_mask] >= 0:
#                     # 새로운 확률 = (이전 상태의 최대 확률) * (현재 행에 j열을 할당할 확률)
#                     new_prob = dp[prev_mask] * arr[row_idx][j]
#
#                     # dp[mask]를 더 큰 값으로 갱신
#                     if dp[mask] < new_prob:
#                         dp[mask] = new_prob
#
#     # 최종 결과: 모든 열을 사용했을 때(모든 비트가 1)의 최대 확률
#     max_prob = dp[(1 << N) - 1]
#
#     print(f"#{tc} {max_prob * 100:.6f}")