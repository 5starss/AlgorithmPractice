# def perm(selected, remain):
#     global min_
#     # 선택하지 않은 원소가 없으면 순열 하나 완성
#     if not remain:
#         #print(selected)
#         tmp = 0
#         for i in range(N):
#             tmp += mat[i][selected[i]]
#         min_ = min(min_, tmp)
#         return min_
#
#     # remain의 각 원소에 대해
#     for i in range(len(remain)):
#         # i번째 원소를 선택
#         pick = remain[i]
#         # 나머지 원소들 (i번째 제외)
#         new_remain = remain[:i] + remain[i+1:]
#         # 재귀 호출
#         perm(selected + [pick], new_remain)
#
# import sys
#
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     mat = [list(map(int, input().split())) for _ in range(N)]
#     remain = list(range(N))
#     selected = []
#     min_ = 9 * N
#     perm(selected, remain)
#     print(f"#{tc} {min_}")

def f(i, N, s):  # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v

    if i == N:  #
        if min_v > s:
            min_v = s
    elif min_v < s:  # 중간 합계가 최소합보다 크면
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]  # 자리교환
            f(i + 1, N, s + arr[i][p[i]])  # i+1자리 결정
            p[i], p[j] = p[j], p[i]  # 원상복구

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 배열의 크기 N x N
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]  # P[i] : i에서 고른 열 번호
    min_v = 10000
    f(0, N, 0)
    print(f"#{tc} {min_v}")