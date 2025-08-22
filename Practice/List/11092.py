import sys

sys.stdin = open('input.txt')

T = int(input())

""" 내장함수 사용
for tc in range(1, T + 1):
    N = int(input())  # 양수의 개수
    arr = list(map(int, input().split()))  # 양수

    max_idx = 0  # 최대값의 위치
    min_idx = arr.index(min(arr))  # 최소 값의 위치. 여러개라면 가장 먼저 나오는 위치

    for i in range(N):
        if max(arr) == arr[i]:  # 최대값이 여러개라면 마지막으로 나오는 위치
            max_idx = i

    print(f"#{tc} {abs(max_idx - min_idx)}")  # 두 값의 차이(절대값)
"""

for tc in range(1, T + 1):
    N = int(input())  # 양수의 개수
    arr = list(map(int, input().split()))  # 양수

    max_value = arr[0]  # 최대값. 0번째 인덱스로 초기화
    max_idx = 0  # 최대값의 위치

    min_value = arr[0]  # 최소값. 0번째 인덱스로 초기화
    min_idx = 0  # 최소값의 위치. 여러개라면 가장 먼저 나오는 위치

    for i in range(1, N):
        if max_value <= arr[i]:  # 최대값이 여러개라면 마지막으로 나오는 위치
            max_value = arr[i]
            max_idx = i
        elif min_value > arr[i]:
            min_value = arr[i]
            min_idx = i

    ans = 0  # 두 값의 차이

    if max_idx > min_idx:  # 절대값
        ans = max_idx - min_idx
    else:
        ans = min_idx - max_idx

    print(f"#{tc} {ans}")
